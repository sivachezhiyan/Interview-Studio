# Interview Studio — validation

Updated 7 October 2026.

## Automated checks

11 integration tests pass. They cover a full 20-question AI session using a simulated Ollama HTTP service, course context, earlier-answer context, report arithmetic, phase coverage, and SQLite persistence. The final answer is verified to affect the overall score.

Practice sessions complete all 20 questions for all 17 streams without invented scores. Twenty distinct prompts are checked for each of the 85 stream/category combinations. Custom courses, invalid profiles, older three/five-question sessions, retry recovery, malformed feedback, duplicate submissions, offline behavior, history, deletion, and request boundaries are covered.

JavaScript syntax check passes.

## Browser checks

- Selected Medical & health sciences → Nursing → Complete interview.
- Completed all 20 questions, observing saved-answer confirmations and feedback only at completion.
- Verified a final report with all 20 responses and a next-practice plan.
- Refreshed and opened My interviews: Nursing showed 20/20 answers and Completed.
- Verified New interview returns to stream selection.
- At 390 px, tested stream search, Arts & science, custom course entry, Admissions & higher studies, and the review step. No horizontal overflow observed.
- Visually reviewed desktop and phone layouts with the new typography and navigation.

## Limits

Ollama and a downloaded model are not installed here. Real model quality, course expertise, and 20-question latency remain unverified. Automated tests use simulated responses, not real AI.

The previous report-download check timed out in the in-app browser. Download and print output remain unverified in a regular browser. Reports are visible and stored locally.

The course catalog is curated, not an exhaustive global directory. Custom course entry supports additional programs. Guided mode supplies response structures, not expert-verified subject answers.
