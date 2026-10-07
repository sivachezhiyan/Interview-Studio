"""Editable discovery catalog. Course names vary by institution; custom entries are supported."""
def stream(key, name, description, courses, topics):
    return {'id': key, 'name': name, 'description': description,
            'courses': courses.split('|'), 'topics': topics.split('|')}

STREAMS = [
    stream('engineering', 'Engineering & technology', 'Build, design, and solve technical problems.',
        'Computer Science Engineering|Information Technology|Artificial Intelligence & Machine Learning|Data Science Engineering|Electronics & Communication Engineering|Electrical & Electronics Engineering|Electrical Engineering|Mechanical Engineering|Civil Engineering|Chemical Engineering|Aerospace Engineering|Aeronautical Engineering|Automobile Engineering|Mechatronics|Robotics & Automation|Biomedical Engineering|Biotechnology Engineering|Environmental Engineering|Industrial Engineering|Production Engineering|Instrumentation & Control|Electronics & Instrumentation|Petroleum Engineering|Mining Engineering|Metallurgical Engineering|Materials Science Engineering|Marine Engineering|Naval Architecture|Textile Engineering|Food Technology|Agricultural Engineering|Polymer Engineering|Ceramic Engineering|Diploma in Engineering',
        'Core concepts|Design & problem solving|Projects & implementation|Quality, reliability & safety|Tools & technology'),
    stream('medical', 'Medical & health sciences', 'Healthcare knowledge, communication, and professional responsibility.',
        'MBBS / Medicine|BDS / Dentistry|Nursing|General Nursing & Midwifery|Pharmacy|Doctor of Pharmacy|Physiotherapy|Occupational Therapy|Veterinary Science|Public Health|Medical Laboratory Technology|Radiology & Imaging Technology|Optometry|Audiology & Speech-Language Pathology|Nutrition & Dietetics|Operation Theatre Technology|Anesthesia Technology|Cardiac Care Technology|Respiratory Therapy|Dialysis Technology|Emergency & Trauma Care|Health Information Management|Clinical Research|Healthcare Administration|Biomedical Science|BAMS / Ayurveda|BHMS / Homeopathy|BUMS / Unani|BSMS / Siddha|BNYS / Naturopathy & Yogic Sciences',
        'Foundational knowledge|Patient communication|Ethics & professional boundaries|Research & evidence appraisal|Safety, teamwork & escalation'),
    stream('commerce', 'Commerce & finance', 'Business numbers, financial reasoning, and commercial awareness.',
        'B.Com General|B.Com Accounting & Finance|B.Com Corporate Secretaryship|B.Com Banking & Insurance|B.Com Taxation|B.Com Computer Applications|B.Com Business Analytics|B.Com International Business|M.Com|Chartered Accountancy|Cost & Management Accounting|Company Secretary|ACCA|Financial Planning|Investment & Portfolio Management|Banking & Financial Services|Economics & Finance|Actuarial Science|Auditing',
        'Accounting & reporting|Financial analysis|Business decisions|Ethics & compliance|Client communication'),
    stream('arts-science', 'Arts & science', 'Explore ideas, research, analysis, and communication.',
        'English Literature|Tamil Literature|Hindi Literature|Linguistics|History|Geography|Political Science|Sociology|Psychology|Philosophy|Economics|Social Work|Anthropology|Archaeology|Mathematics|Statistics|Physics|Chemistry|Botany|Zoology|Microbiology|Biochemistry|Biotechnology|Environmental Science|Geology|Astronomy|Forensic Science|Home Science|Food Science|Library & Information Science|International Relations|Public Administration|Gender Studies|Development Studies',
        'Subject knowledge|Research methods|Analysis & interpretation|Communication & argument|Practical applications'),
    stream('computing', 'Computer applications & IT', 'Software, infrastructure, data, and digital security.',
        'BCA|MCA|B.Sc Computer Science|M.Sc Computer Science|Information Technology|Software Development|Web Development|Mobile App Development|Data Analytics|Data Science|Artificial Intelligence|Cybersecurity|Cloud Computing|Computer Networking|DevOps|Software Testing|Database Administration|Game Development|UI Engineering|IT Support',
        'Programming & fundamentals|Systems & architecture|Projects & debugging|Data & security|Tools & workflows'),
    stream('management', 'Business & management', 'Lead teams, understand customers, and make decisions.',
        'BBA|BBM|BMS|MBA General|Marketing|Human Resource Management|Finance Management|Operations Management|Business Analytics|International Business|Entrepreneurship|Project Management|Supply Chain Management|Retail Management|Healthcare Management|Event Management|Sports Management|Rural Management|Digital Marketing',
        'Business strategy|People & leadership|Operations & execution|Customers & markets|Data-driven decisions'),
    stream('law', 'Law & public policy', 'Reason carefully, communicate clearly, and act responsibly.',
        'LLB|BA LLB|BBA LLB|B.Com LLB|LLM|Corporate Law|Criminal Law|Constitutional Law|Intellectual Property Law|Cyber Law|International Law|Human Rights|Environmental Law|Public Policy|Legal Studies|Paralegal Studies',
        'Legal reasoning|Research & interpretation|Ethics & confidentiality|Advocacy & communication|Policy analysis'),
    stream('education', 'Education & teaching', 'Support learning, inclusion, and classroom communication.',
        'B.Ed|M.Ed|D.El.Ed|B.El.Ed|Early Childhood Education|Special Education|Educational Psychology|Physical Education|Educational Technology|Curriculum & Instruction|Teacher Training|TESOL / English Language Teaching|Education Administration',
        'Teaching practice|Lesson planning|Assessment & feedback|Inclusion & learner support|Classroom communication'),
    stream('design', 'Design & creative arts', 'Bring ideas to life through craft, process, and storytelling.',
        'Graphic Design|Communication Design|UI/UX Design|Interaction Design|Product Design|Industrial Design|Fashion Design|Textile Design|Interior Design|Animation|Visual Effects|Game Art|Fine Arts|Painting|Sculpture|Photography|Film Design|Music|Dance|Theatre|Performing Arts',
        'Portfolio & process|Creative problem solving|Tools & craft|Audience & usability|Critique & collaboration'),
    stream('media', 'Media & communication', 'Tell stories, understand audiences, and verify information.',
        'Journalism|Mass Communication|Visual Communication|Advertising|Public Relations|Film & Television|Digital Media|Content Writing|Broadcast Journalism|Media Production|Corporate Communication|Publishing',
        'Storytelling & writing|Research & verification|Audience strategy|Production & tools|Ethics & communication'),
    stream('agriculture', 'Agriculture & environment', 'Work with food systems, natural resources, and sustainability.',
        'Agriculture|Horticulture|Forestry|Fisheries Science|Animal Husbandry|Dairy Technology|Agribusiness Management|Soil Science|Plant Pathology|Entomology|Seed Technology|Sustainable Agriculture|Environmental Management|Wildlife Conservation|Marine Biology|Water Resource Management',
        'Core science|Fieldwork & observation|Sustainable practices|Data & research|Community communication'),
    stream('architecture', 'Architecture & planning', 'Shape spaces, places, and the built environment.',
        'B.Arch|M.Arch|Urban Planning|Regional Planning|Landscape Architecture|Urban Design|Building Technology|Construction Management|Interior Architecture|Sustainable Architecture|Architectural Conservation',
        'Design thinking|Portfolio & presentation|Site & context|Materials & construction|Sustainability & accessibility'),
    stream('hospitality', 'Hospitality & tourism', 'Create thoughtful service and guest experiences.',
        'Hotel Management|Hospitality Administration|Culinary Arts|Bakery & Patisserie|Travel & Tourism|Tourism Management|Food & Beverage Service|Front Office Management|Housekeeping Operations|Cruise Hospitality|Event & Leisure Management',
        'Guest service|Operations & standards|Problem resolution|Teamwork & communication|Planning & commercial awareness'),
    stream('aviation', 'Aviation, logistics & transport', 'Coordinate people, operations, and reliable movement.',
        'Aviation Management|Airport Operations|Cabin Crew Training|Aircraft Maintenance|Pilot Training|Air Cargo Management|Logistics & Supply Chain|Shipping & Port Management|Transport Management|Warehouse Management|Nautical Science',
        'Operational fundamentals|Safety & escalation|Planning & coordination|Service & communication|Quality & improvement'),
    stream('vocational', 'Vocational & skilled trades', 'Show practical skills, reliability, and workmanship.',
        'Electrician|Fitter|Welder|Plumber|Carpentry|Machining & CNC|Automotive Service|Refrigeration & Air Conditioning|Electronics Technician|Computer Operator & Programming Assistant|Laboratory Technician|Beauty & Wellness|Apparel & Garment Technology|Retail Operations|Office Administration|Renewable Energy Technician',
        'Trade fundamentals|Tools & workmanship|Safety & procedure|Troubleshooting|Customer & team communication'),
    stream('sports', 'Sports & wellness', 'Coaching, performance, teamwork, and healthy practice.',
        'Sports Science|Sports Coaching|Physical Education|Exercise Science|Fitness Training|Sports Psychology|Sports Nutrition|Yoga Studies|Recreation Management',
        'Foundational knowledge|Coaching & communication|Planning & assessment|Ethics & boundaries|Teamwork & leadership'),
    stream('other', 'Other / interdisciplinary', 'Create a path for your own course or career transition.',
        'Interdisciplinary Studies|General Studies|Research Studies|Career Transition|Civil Services Preparation|Entrepreneurship & Self-employment',
        'Core knowledge|Applied problem solving|Projects & experience|Communication|Professional judgment'),
]

FOCUSES = [
    {'id': 'balanced', 'name': 'Complete interview', 'description': 'A balanced mix of your background, subject knowledge, practical thinking, and teamwork.'},
    {'id': 'subject', 'name': 'Subject & technical knowledge', 'description': 'Explain concepts, connect ideas, and apply knowledge from your course.'},
    {'id': 'behavioral', 'name': 'HR & behavioral', 'description': 'Practice your introduction, motivations, communication, and workplace examples.'},
    {'id': 'practical', 'name': 'Practical & scenario questions', 'description': 'Think through realistic situations, decisions, projects, and trade-offs.'},
    {'id': 'admission', 'name': 'Admissions & higher studies', 'description': 'Discuss academic interests, research readiness, and why this course fits you.'},
]
PHASES = ['Your background', 'Subject foundations', 'Applied thinking', 'Working with others', 'Reflection & next steps']

# Twenty distinct prompts; course and chosen topic ground the practice guide.
PROMPTS = [
    ('Introduce yourself and explain how your background connects to {course}.', 'Connect your background, relevant experience, and current goal.'),
    ('What first drew you to {course}, and what keeps you interested?', 'Explain your motivation with a real learning experience.'),
    ('Which experience best shows your readiness for an opportunity in {course}?', 'Describe your own contribution and what you learned.'),
    ('What would you like an interviewer to understand about your interest in {topic}?', 'Connect a specific interest to the opportunity you want.'),
    ('Explain a foundational concept from {course} to someone new to the subject.', 'Define it accurately, give an example, and check understanding.'),
    ('Compare two approaches you have learned in {course}. When is each useful?', 'State their assumptions, strengths, and limitations.'),
    ('What is a common misconception about {topic}, and how would you clarify it?', 'Distinguish the misconception from a supported explanation.'),
    ('How would you check whether a claim in {course} is trustworthy?', 'Explain evidence quality, verification, and uncertainty.'),
    ('Describe how you would approach an unfamiliar task involving {topic}.', 'Clarify the goal, constraints, steps, and success criteria.'),
    ('Tell me about a project, assignment, or placement connected to {course}.', 'Use a real example: goal, action, result, and learning.'),
    ('How would you choose between two solutions to a problem in {course}?', 'Compare criteria, trade-offs, and how you would test assumptions.'),
    ('If your first approach to a task involving {topic} failed, what would you do next?', 'Investigate systematically and explain when to seek help.'),
    ('Describe a time you worked with someone whose approach differed from yours.', 'Explain how you listened, agreed on a goal, and contributed.'),
    ('How would you explain a complex idea from {course} to a non-specialist?', 'Adapt your language and use an example without losing accuracy.'),
    ('What would you do if you were asked to act beyond your knowledge or responsibility?', 'Recognize limits, communicate concerns, and seek appropriate support.'),
    ('How would you manage competing deadlines during a project related to {course}?', 'Prioritize by impact and dependencies; communicate realistic commitments.'),
    ('Tell me about feedback that changed how you approached your work or studies.', 'Describe the change you made and evidence of improvement.'),
    ('Which skill in {course} would you most like to improve, and how will you practice it?', 'Choose a specific gap and a realistic learning plan.'),
    ('What could you contribute to a team working on {topic}?', 'Support your strengths with genuine examples; avoid unsupported claims.'),
    ('What would you ask the interviewer about the role, course, or team?', 'Ask thoughtful questions that help you assess fit and expectations.'),
]

def practice_question(s):
    i = len(s['turns'])
    course = s['course']
    topics = s.get('topics') or ['your chosen field']
    topic = topics[(i // 4) % len(topics)]
    prompt, hint = PROMPTS[i]
    focus = s.get('interview_focus', 'balanced')
    # Focus-specific wording keeps each route meaningful, while preserving distinct questions.
    if focus == 'subject':
        prompt = [
            'Which foundational idea in {course} do you find most important, and why?',
            'How did you build your understanding of {topic}?',
            'Describe an assignment that tested your knowledge of {course}.',
            'Which prerequisite concepts are essential to understand {topic}?',
        ][i] if i < 4 else prompt
    elif focus == 'behavioral' and 4 <= i < 12:
        prompt, hint = [
            ('Describe a time you learned something difficult.', 'Explain your approach and progress.'),
            ('Tell me about a mistake and how you took responsibility.', 'Focus on your action and learning.'),
            ('Describe a time you adapted to an unexpected change.', 'Explain how you reset priorities.'),
            ('How do you handle feedback you disagree with?', 'Show listening, clarification, and reflection.'),
            ('Tell me about a time you took initiative.', 'Use a real example and distinguish your contribution.'),
            ('Describe how you helped a teammate who was struggling.', 'Explain support without claiming their work.'),
            ('How do you stay motivated during repetitive tasks?', 'Share a practical method and example.'),
            ('Describe a time you had to ask for help.', 'Explain how you recognized your limits.'),
        ][i-4]
    elif focus == 'admission':
        prompt = prompt.replace('opportunity', 'higher-study opportunity').replace('role, course, or team', 'program, supervisor, or research environment')
        if i == 9:
            prompt = 'What research question would you like to explore in {course}, and how would you begin?'
    elif focus == 'practical' and i < 4:
        prompt = [
            'Describe a practical task in {course} that you would feel ready to take on.',
            'What information would you collect before starting a task involving {topic}?',
            'Tell me about a hands-on assignment or project in {course}.',
            'How would you define success for a practical task involving {topic}?',
        ][i]
    question = prompt.format(course=course, topic=topic)
    reference = f'Build your response around this: {hint} Use a genuine example from {course}, explain your own reasoning, and acknowledge uncertainty. This is a response structure, not a verified subject answer.'
    return [question, hint, reference]
