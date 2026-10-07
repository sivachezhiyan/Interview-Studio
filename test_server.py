import json
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from server import App, Store, Ollama, METRICS, CATEGORIES, Problem, make_handler
from catalog import STREAMS, FOCUSES, practice_question

class FakeOllamaHandler(BaseHTTPRequestHandler):
    requests = []
    invalid = False
    def log_message(self, *_): pass
    def do_GET(self):
        self.send_response(200); self.end_headers()
        self.wfile.write(json.dumps({'models':[{'name':'qwen3:4b'}]}).encode())
    def do_POST(self):
        body=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        self.requests.append(body)
        if 'question' in body['format']['properties']:
            context=json.loads(body['messages'][1]['content'])
            result={'question':'Follow-up on your answer' if context['previous_turns'] else 'Explain a transaction.', 'focus':'Use an example.'}
        else:
            result={'scores':{m:8 for m in METRICS},'strengths':['Clear explanation.'],'improvements':['Add a trade-off.'],'improved_answer':'A transaction groups changes atomically.'}
            if self.invalid: result['scores']['relevance']=100
        self.send_response(200); self.end_headers()
        self.wfile.write(json.dumps({'message':{'content':json.dumps(result)}}).encode())

class FlowTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        FakeOllamaHandler.requests=[]; FakeOllamaHandler.invalid=False
        self.ollama=ThreadingHTTPServer(('127.0.0.1',0),FakeOllamaHandler)
        threading.Thread(target=self.ollama.serve_forever,daemon=True).start()
        self.app=App(Store(Path(self.tmp.name)/'db.sqlite'),Ollama(url=f'http://127.0.0.1:{self.ollama.server_port}'))
        self.http=ThreadingHTTPServer(('127.0.0.1',0),make_handler(self.app))
        threading.Thread(target=self.http.serve_forever,daemon=True).start()
        self.base=f'http://127.0.0.1:{self.http.server_port}'
    def tearDown(self):
        for server in [self.http,self.ollama]: server.shutdown();server.server_close()
        self.tmp.cleanup()
    def request(self,path,method='GET',body=None,headers=None):
        req=Request(self.base+path,json.dumps(body).encode() if body is not None else None,headers or {'Content-Type':'application/json'},method=method)
        try:
            with urlopen(req) as r: return json.load(r)
        except HTTPError as error:
            error.close()
            raise
    def start(self,mode='ai',category='software',length=3):
        return self.request('/api/interviews','POST',{'mode':mode,'category':category,'length':length,'difficulty':'Beginner'})
    def answer(self,s):
        return self.request('/api/interviews/'+s['id']+'/answer','POST',{'answer':'I use a database transaction to keep changes atomic and consistent.','revision':s['revision']})
    def test_ai_flow_adaptive_report_and_persistence(self):
        s=self.start()
        self.assertEqual(s['current']['question'],'Explain a transaction.')
        for i in range(3):
            s=self.answer(s)
            self.assertEqual(len(s['turns']),i+1)
            if i<2:
                s=self.request('/api/interviews/'+s['id']+'/next','POST',{})
                self.assertEqual(s['current']['question'],'Follow-up on your answer')
        self.assertEqual(s['status'],'completed')
        self.assertEqual(s['report']['overall'],80)
        self.assertEqual(s['report']['dimensions'],{m:8.0 for m in METRICS})
        reopened=Store(Path(self.tmp.name)/'db.sqlite').get(s['id'])
        self.assertEqual(len(reopened['turns']),3)
        qrequests=[r for r in FakeOllamaHandler.requests if 'question' in r['format']['properties']]
        self.assertEqual(len(json.loads(qrequests[1]['messages'][1]['content'])['previous_turns']),1)
        self.assertFalse(qrequests[0]['stream'])
        self.assertIn('untrusted',qrequests[0]['messages'][0]['content'])
        self.assertEqual(self.request('/api/interviews')[0]['overall'],80)
        self.request('/api/interviews/'+s['id'],'DELETE',{})
        self.assertEqual(self.request('/api/interviews'),[])
    def test_practice_all_categories_no_fabricated_scores(self):
        for category in CATEGORIES:
            s=self.start('practice',category,5)
            for i in range(5):
                s=self.answer(s)
                self.assertIsNone(s['report']['overall'])
                if i<4:s=self.request('/api/interviews/'+s['id']+'/next','POST',{})
            self.assertEqual(s['status'],'completed')
        self.assertEqual(FakeOllamaHandler.requests,[])
    def test_duplicate_submission_rejected(self):
        s=self.start('practice'); self.answer(s)
        with self.assertRaises(HTTPError) as error:self.answer(s)
        self.assertEqual(error.exception.code,409)
        self.assertEqual(len(self.app.store.get(s['id'])['turns']),1)
    def test_invalid_model_feedback_leaves_answer_retryable(self):
        s=self.start();FakeOllamaHandler.invalid=True
        with self.assertRaises(HTTPError) as error:self.answer(s)
        self.assertEqual(error.exception.code,503)
        self.assertEqual(self.app.store.get(s['id'])['turns'],[])
        FakeOllamaHandler.invalid=False
        self.assertEqual(len(self.answer(s)['turns']),1)
    def test_next_failure_preserves_saved_feedback(self):
        s=self.answer(self.start())
        original=self.app.ai.generate
        self.app.ai.generate=lambda *args: (_ for _ in ()).throw(Problem('offline',503))
        with self.assertRaises(HTTPError):self.request('/api/interviews/'+s['id']+'/next','POST',{})
        saved=self.app.store.get(s['id'])
        self.assertEqual(len(saved['turns']),1); self.assertIsNone(saved['current'])
        self.app.ai.generate=original
        self.assertIsNotNone(self.request('/api/interviews/'+s['id']+'/next','POST',{})['current'])
    def test_input_validation_and_cross_origin(self):
        s=self.start('practice')
        for answer in ['', ' '*5, 'x'*6001, 10]:
            with self.assertRaises(HTTPError) as e:self.request('/api/interviews/'+s['id']+'/answer','POST',{'answer':answer,'revision':0})
            self.assertEqual(e.exception.code,400)
        with self.assertRaises(HTTPError) as e:self.request('/api/interviews','POST',{}, {'Content-Type':'application/json','Origin':'https://untrusted.example'})
        self.assertEqual(e.exception.code,403)
        with self.assertRaises(HTTPError) as e:self.request('/api/interviews','POST',{'mode':'ai','category':'invalid','length':3,'difficulty':'Beginner'})
        self.assertEqual(e.exception.code,400)
    def test_server_assets_and_no_database_exposure(self):
        for path in ['/','/app.js','/style.css']:
            with urlopen(self.base+path) as r:
                self.assertEqual(r.status,200);self.assertIn("default-src 'self'",r.headers['Content-Security-Policy'])
        with self.assertRaises(HTTPError) as e:self.request('/data/interviews.sqlite3')
        self.assertEqual(e.exception.code,404)
    def test_offline_model(self):
        self.app.ai=Ollama(url='http://127.0.0.1:1')
        self.assertFalse(self.request('/api/status')['available'])
        with self.assertRaises(HTTPError) as e:self.start()
        self.assertEqual(e.exception.code,503)
        self.assertEqual(self.start('practice')['status'],'active')

    def modern(self, mode='practice', stream=None, **extra):
        stream=stream or STREAMS[0]
        return self.request('/api/interviews','POST', {'stream':stream['id'], 'course':stream['courses'][0],
            'interview_focus':'balanced', 'topics':stream['topics'], 'difficulty':'Beginner', 'mode':mode, **extra})
    def test_20_question_flow_and_late_answer_report(self):
        s=self.modern('ai')
        self.assertEqual(s['length'],20)
        for i in range(20):
            s=self.answer(s)
            if i<19:
                self.assertEqual(s['status'],'active')
                s=self.request('/api/interviews/'+s['id']+'/next','POST',{})
        self.assertEqual(s['status'],'completed')
        self.assertEqual(s['report']['overall'],80)
        self.assertEqual([p['answered'] for p in s['report']['phases']],[4]*5)
        self.assertEqual(len(s['report']['action_plan']),2)
        self.assertEqual(len(self.app.store.get(s['id'])['turns']),20)
        contexts=[json.loads(r['messages'][1]['content']) for r in FakeOllamaHandler.requests]
        self.assertTrue(all(c['course']==STREAMS[0]['courses'][0] for c in contexts))
        self.assertEqual(contexts[-2]['question_number'],20)
        self.assertEqual(len(contexts[-2]['previous_turns']),19)
        # The last answer must contribute, not just the earliest feedback.
        raw=self.app.store.get(s['id']);raw['turns'][-1]['evaluation']['scores']={m:0 for m in METRICS}
        self.assertEqual(self.app.report(raw)['overall'],76)
    def test_catalog_routes_and_all_practice_paths(self):
        catalog=self.request('/api/catalog')
        self.assertEqual(len(catalog['streams']),17)
        for stream in STREAMS:
            for focus in FOCUSES:
                state={'course':stream['courses'][0],'topics':stream['topics'],'interview_focus':focus['id'],'turns':[]}
                questions=[]
                for i in range(20):
                    state['turns']=[None]*i
                    questions.append(practice_question(state)[0])
                self.assertEqual(len(set(questions)),20)
            s=self.modern(stream=stream)
            for i in range(20):
                s=self.answer(s)
                if i<19:s=self.request('/api/interviews/'+s['id']+'/next','POST',{})
            self.assertEqual(s['status'],'completed')
            self.assertIsNone(s['report']['overall'])
    def test_custom_course_and_invalid_profile(self):
        s=self.modern(course='Computational Biology',custom_course=True)
        self.assertEqual(s['course'],'Computational Biology')
        for extra in [{'course':'Not listed'}, {'topics':[]}, {'topics':['unrelated']}, {'interview_focus':'unknown'}, {'course':' '*5}]:
            with self.assertRaises(HTTPError) as e:self.modern(**extra)
            self.assertEqual(e.exception.code,400)

if __name__=='__main__':unittest.main(verbosity=2)
