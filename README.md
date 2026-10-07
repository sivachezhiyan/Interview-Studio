# Interview Studio

Private, local interview preparation for students, graduates, and professionals.

## Start

Install Python 3.10 or newer. No Python packages are required. Open a terminal in this folder and run:

```text
python server.py
```

On Windows, you can double-click `start.cmd`. Open http://127.0.0.1:8765 in your browser. Keep the terminal open. Press Ctrl+C to stop. If the port is busy, use `python server.py --port 8766`.

## Your interview journey

1. **Choose a stream:** 17 streams, from engineering and medical to commerce, arts and science, law, education, design, agriculture, and skilled trades.
2. **Choose your course:** 298 listed options with search, plus **Enter my own course**. Names differ by institution; this is a curated starting catalog, not a claim to list every course worldwide.
3. **Choose a category:** Complete interview, Subject & technical knowledge, HR & behavioral, Practical & scenario questions, or Admissions & higher studies. Select relevant stream-specific focus areas.
4. **Review and start:** choose difficulty and local AI or guided practice. All new sessions contain **20 questions**.
5. **Answer at your own pace:** one question at a time; a saved-answer confirmation appears after submission. Feedback is shown after all 20 questions. Use **Save & leave** and resume from **My interviews**.
6. **Review your report:** four score dimensions in AI mode, overall score, five interview phases, strengths, improvements, an action plan, and all 20 answers with suggestions.

The five phases are Your background, Subject foundations, Applied thinking, Working with others, and Reflection & next steps. The selected category changes their emphasis. Typical answering time is roughly 30–60 minutes, plus local generation time; there is no timer.

## Enable local AI

Install [Ollama](https://ollama.com/download), open it, then download a model:

```text
ollama pull qwen3:4b
```

Keep Ollama running. If needed, start it with `ollama serve`. In the app, open **Connect local AI** and check the connection. Choose Local AI when starting an interview.

For a smaller model, run `ollama pull qwen3:1.7b`, then `python server.py --model qwen3:1.7b`. Model quality and speed depend on your PC. Downloads need internet and several GB of space; downloaded local models and all UI assets can work offline. No paid API key is required. Only use local models for the offline workflow.

The app connects to Ollama at `http://127.0.0.1:11434`. Each model request allows 180 seconds. The four-part rubric scores relevance, clarity, completeness, and technical/subject accuracy from 0–10. Overall score averages every dimension across every answer and scales to 100. These are practice estimates, not validated hiring predictions or personality assessments. Verify technical claims with reliable materials. Healthcare, legal, and financial questions are educational interview scenarios, not real-world professional advice.

Guided practice works immediately without a model. It supplies 20 distinct course-context prompts and response structures, not expert-verified subject answers. It does not evaluate correctness or give numerical scores. Difficulty affects AI mode only.

## Local data and reliability

SQLite history is created at `data/interviews.sqlite3`. Use `--db PATH` to choose another location. Back up the file while the server is stopped. Existing older three- and five-question sessions remain readable and resumable.

Each submitted answer and its evaluation are persisted before the next question is generated. Failed model calls can be retried. Duplicate/stale submissions are rejected. Browser drafts recover after refresh; successful submission clears the draft. Deleting an interview removes its database record and drafts in the current browser. Data is not encrypted.

This is a single-user local application, not a public hosting deployment. It binds to loopback and rejects cross-origin mutations. No account, microphone, camera, subscription, CDN assets, or cloud sync is needed.

## Design

Three-step setup, searchable streams and courses, visible progress, plain-language mode descriptions, a dedicated How it works page, responsive layouts, and clear actions. Georgia headings pair with Segoe UI/Calibri body text, using offline system-font fallbacks.

## Project files

- `server.py`: local HTTP API, SQLite, Ollama integration, validation, reports.
- `catalog.py`: 17 streams, 298 course options, category definitions, and practice-question generation.
- `static/`: HTML, CSS, and JavaScript interface.
- `test_server.py`: integration tests using temporary SQLite and a simulated Ollama endpoint.
- `start.cmd`: Windows launcher.

## Tests

```text
python -m unittest -v test_server.py
```

See `VALIDATION.md` for completed checks and limits. A real-model smoke test still needs Ollama: complete a 20-question AI session and inspect whether course-specific questions and feedback are appropriate. Test download and printing in your usual browser before presenting.

API references: [Ollama chat](https://docs.ollama.com/api/chat) and [structured outputs](https://docs.ollama.com/capabilities/structured-outputs).
