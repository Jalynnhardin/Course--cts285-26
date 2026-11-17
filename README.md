# DataMan Module 4 - Memory Bank and Curator Retrieval

## Purpose and selected product slice
This is a minimal text-only prototype for the Memory Bank and Curator Retrieval product slice from the M4 Design Investigation Record. A curator can create a practice set with up to 10 problems, a learner can complete a two-attempt practice session, and a curator can retrieve the specific problems missed.

The investigation changed the design from storing only a final score to preserving individual Attempt records and session information. The prototype tests that decision. See [`docs/m4-design-investigation-record.md`](docs/m4-design-investigation-record.md) for the full investigation evidence and unresolved question.

## Run the prototype
Use Python 3. From the `DataMan_Module4` folder, run:

```bash
python app.py
```

Starter data includes Practice Set `S1` with five sample problems (P1-P5). Choose menu option `3` to practice. The program displays a session ID. After practice, choose option `4` and enter that session ID to retrieve the curator report.

## Run the tests
From the same folder, run:

```bash
python -m unittest discover -s tests -v
```

The tests check the 10-problem limit, first/second attempt behavior, exact missed-problem retrieval, and persistence of a first attempt after data is saved and reloaded.

## Three layer responsibilities
- **Text interface — `app.py`:** receives menu choices and learner answers, then displays messages and reports. It calls the logic and store modules.
- **Business logic — `dataman/logic.py`:** applies reusable rules for the 10-problem limit, session creation, attempt order, answer checking, the two-attempt limit, and curator reporting. It does not prompt, print, or read/write files.
- **Stubbed data layer — `dataman/store.py`:** loads and saves the prototype data as JSON. This is the only module that handles persistence. It can be replaced with database operations in Module 5 without moving storage code into the interface or business rules.

## Deliberate state and data choices
- **PracticeSet:** set ID, name, and problem IDs.
- **Problem:** problem ID, question, and correct answer.
- **Session:** session ID, learner label, practice set ID, and status.
- **Attempt:** session ID, problem ID, try number, learner answer, and correctness.

The interface saves the session when it starts and saves each attempt immediately after it is recorded. This tests the investigation finding that a first attempt must survive if the program closes. The curator report uses the Attempt records to distinguish first-try success, second-try success, and problems missed after two incorrect answers.

For this small JSON prototype, each PracticeSet contains a list of problem IDs. A relational database may need a separate PracticeSetProblem linking table if problems can be reused across sets; that relationship should be confirmed during Module 5 database design.

## Acceptance criteria demonstrated
1. **Maximum set size:** a practice set cannot contain more than 10 problems. The business logic rejects an 11th addition.
2. **Attempt history:** a first attempt is saved to the JSON data file before the learner moves on. A test saves and reloads the data and verifies that the first attempt and in-progress session remain present.
3. **Two-attempt behavior:** the learner can try a problem a second time after a wrong first answer; the business logic rejects attempt 2 if attempt 1 is missing or already correct.
4. **Curator retrieval:** the report identifies the specific problem IDs missed after two incorrect attempts instead of showing only a final score.

These criteria trace to the investigation's findings on preserving attempt number and answer status, the logic boundary for the 10-problem limit, and the requirement/backlog direction to preserve learner practice activity for later retrieval.

## Intentionally stubbed work
- JSON is temporary local persistence, not the final database.
- There is no login, verified learner identity, role security, or multi-curator access control.
- The command-line interface is used instead of Flask; Flask begins in Module 5.
- Answers are whole numbers only.
- There is no edit/delete workflow for practice sets or problems.
- The prototype records unfinished sessions, but does not yet offer a resume-session workflow.

## Evaluation, revision, and unresolved questions
The tests confirm that attempt records retain problem ID, try number, learner answer, and correctness, and that the curator can retrieve a problem missed twice. The persistence test also confirms that a saved first attempt remains in the data after reloading it.

**Revision made while testing:** the business logic now rejects a second attempt if the first attempt was already correct. This keeps the two-attempt rule in the reusable logic layer instead of relying only on the current interface to prevent an invalid second try.

**Unresolved questions carried forward from the investigation:** should a learner be able to retrieve and resume an unfinished session after closing the program, and what permissions should multiple curators have when viewing learner history? The prototype preserves unfinished session data but does not implement resumption or access permissions.

## Module 5 handoff
Carry forward the product slice, acceptance criteria, business rules, and PracticeSet/Problem/Session/Attempt state model. Replace `dataman/store.py` JSON operations with database operations while keeping the rules in `dataman/logic.py` independent of Flask. The next design question is: **How should unfinished sessions be retrieved and resumed while protecting the learner's saved attempt history?**
