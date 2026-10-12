# DataMan Product Backlog

## Sources

This backlog uses the requirements register and the Module 3
backlog-triage and product-owner decision records. The requirements
register includes FR-7, elicited in Module 2, for preserving learner
progress between authenticated sessions; its data scope and retention
details remain unresolved.

## Priority Order

1.  US-01
2.  US-02
3.  US-03
4.  US-04
5.  US-05
6.  US-06
7.  US-07

## Stories

### US-01 --- Check an arithmetic answer and give immediate feedback

**Requirement ID:** FR-1, NFR-1, NFR-2, NFR-3

**User Story:** As a learner, I want to submit an arithmetic problem and
answer and receive immediate feedback so that I can check whether my
answer is correct.

**Acceptance Criteria:**

-   Given an arithmetic problem and a submitted answer, when the answer
    is correct, then the system indicates that it is correct.
-   Given an arithmetic problem and a submitted answer, when the answer
    is incorrect, then the system indicates that it is incorrect.
-   Given an Answer Checker problem, when the problem uses one- or
    two-digit numbers, then the system accepts the problem.
-   Given an Answer Checker problem, when the submitted answer contains
    one, two, or three digits, then the system accepts the answer for
    checking.
-   Given a subtraction problem whose result would be negative, when the
    problem is submitted, then the system rejects it.

**Relative Effort:** M --- This combines the core checking behavior with
several input constraints, so it is broader than the retry and results
stories.

**Dependency / Constraint:** The arithmetic answer-checking flow must be
available. NFR-1, NFR-2, and NFR-3 constrain the supported inputs and
problems.

**Priority:** 1

**Readiness:** Move Forward

**Priority Rationale:** Immediate answer feedback is high value and was
explicitly identified as necessary for the first usable release in the
M3 triage record. The confirmed requirement and bounded input
constraints make this a comparatively ready core capability.

------------------------------------------------------------------------

### US-02 --- Allow a second attempt after an incorrect answer

**Requirement ID:** FR-2

**User Story:** As a learner, I want another attempt after an incorrect
answer so that I can try to solve the problem before seeing the correct
result.

**Acceptance Criteria:**

-   Given a learner submits an incorrect answer on the first attempt,
    when the system responds, then it allows one more attempt before
    showing the correct result.
-   Given a learner submits an incorrect answer on the second attempt,
    when the system responds, then it displays the correct result.
-   Given a learner submits a correct answer on either allowed attempt,
    when the system responds, then it indicates that the answer is
    correct.

**Relative Effort:** S --- The behavior is narrowly scoped and follows
the answer-checking flow.

**Dependency / Constraint:** US-01 answer-checking flow.

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** Retry behavior is a confirmed, high-value
learning interaction. The M3 triage record says to refine the retry
story, but the requirements register provides the two-attempt rule;
implementation should still be checked against these explicit outcomes.

------------------------------------------------------------------------

### US-03 --- Give feedback on stored-practice answers

**Requirement ID:** FR-5, FR-6, NFR-5

**User Story:** As a learner, I want to store practice problems and
receive feedback when I answer them so that I can revisit problems and
check my work.

**Acceptance Criteria:**

-   Given fewer than 10 problems are stored, when a learner stores a
    practice problem, then the problem is available for later practice.
-   Given 10 problems are already stored, when a learner attempts to
    store another problem, then the system does not store an eleventh
    problem. The exact user-facing message or recovery behavior remains
    to be decided.
-   Given a stored practice problem is being answered, when the learner
    submits an answer, then the system indicates whether the answer is
    correct or incorrect.

**Relative Effort:** M --- Storing, retrieving, and checking stored
problems is broader than a single feedback interaction.

**Dependency / Constraint:** The Memory Bank behavior and its 10-problem
capacity limit. The requirements do not define the user-facing behavior
when the limit is reached.

**Priority:** 3

**Readiness:** Refine

**Priority Rationale:** Reusable practice and immediate feedback have
clear learner value, but the full storage interaction and capacity-limit
behavior need clarification before the story is fully ready. This
combines FR-5 and FR-6 because the feedback criterion applies
specifically to stored practice; split further if implementation
planning shows separate work.

------------------------------------------------------------------------

### US-04 --- Show Answer Checker session results

**Requirement ID:** FR-3

**User Story:** As a learner, I want to see how many answers I got right
and how many problems I attempted so that I can review my practice
session.

**Acceptance Criteria:**

-   Given a learner completes the documented 10-problem Answer Checker
    session, when the session ends, then the system displays the number
    of correct answers.
-   Given a learner completes the documented 10-problem Answer Checker
    session, when the session ends, then the system displays the number
    of problems attempted.

**Relative Effort:** S --- The result is limited to two session totals.

**Dependency / Constraint:** Answer Checker session completion and
tracking of correct answers and attempted problems. The source describes
results after 10 problems.

**Priority:** 4

**Readiness:** Move Forward

**Priority Rationale:** Session results provide useful learner feedback,
but the M3 records emphasize getting the core interaction working first.
This story has limited scope and no identified unresolved dependency
beyond session tracking.

------------------------------------------------------------------------

### US-05 --- Play Number Guesser

**Requirement ID:** FR-4

**User Story:** As a learner, I want to guess a secret number and
receive range hints so that I can narrow down the answer and see how
many guesses I needed.

**Acceptance Criteria:**

-   Given a new Number Guesser game begins, when the game selects its
    secret number, then the number is between 9 and 100 inclusive.
-   Given the learner submits a guess lower than the secret number, when
    the guess is evaluated, then the system provides a hint indicating
    the secret number is higher.
-   Given the learner submits a guess higher than the secret number,
    when the guess is evaluated, then the system provides a hint
    indicating the secret number is lower.
-   Given the learner guesses the secret number, when the guess is
    evaluated, then the system indicates success and displays the total
    number of guesses.

**Relative Effort:** M --- The game requires secret-number selection,
repeated guess evaluation, hints, and a final count.

**Dependency / Constraint:** The documented Number Guesser rules. The
acceptance criteria interpret "range hints" as higher/lower feedback
consistent with the stated goal; confirm this wording against the manual
if its exact hint behavior differs.

**Priority:** 5

**Readiness:** Move Forward

**Priority Rationale:** This is a confirmed learning activity with
bounded behavior, but the triage record gives stronger release evidence
for immediate answer feedback and retry behavior. No specific dependency
is identified.

------------------------------------------------------------------------

### US-06 --- Preserve saved learner progress between authenticated sessions

**Requirement ID:** FR-7

**User Story:** As an authenticated learner, I want my saved progress to
remain available when I return in a later session so that I do not lose
the progress I have made.

**Acceptance Criteria:**

-   Given an authenticated learner has saved progress, when the learner
    leaves and later starts another authenticated session, then the
    saved progress is available to that learner.
-   Given a learner starts a later authenticated session, when the
    system retrieves saved progress, then it does not present another
    learner's saved progress as theirs.

**Relative Effort:** L --- This is larger than the individual practice
activities because it depends on a defined identity/session approach and
a clear persistence scope.

**Dependency / Constraint:** Identity/session approach. The exact
progress data to preserve, retention duration, and activities covered
are unresolved.

**Priority:** 6

**Readiness:** Refine

**Priority Rationale:** The stakeholder requirement is confirmed and
potentially high value, but the triage record specifically flags
identity/session readiness as a dependency. Keep the item visible while
resolving those questions rather than treating it as ready to implement.

------------------------------------------------------------------------

### US-07 --- Power off after inactivity

**Requirement ID:** NFR-4

**User Story:** As a user, I want the device to power off after
approximately five minutes of inactivity so that it does not remain on
indefinitely when unused.

**Acceptance Criteria:**

-   Given the device is idle, when approximately five minutes pass
    without use, then the device powers off automatically.

**Relative Effort:** M --- This behavior may involve device-level
inactivity handling and should be estimated against the implementation
context.

**Dependency / Constraint:** The requirement is stated as a device
behavior in the DataMan manual; confirm the relevant inactivity events
and acceptable timing tolerance before implementation.

**Priority:** 7

**Readiness:** Refine

**Priority Rationale:** The requirement is confirmed, but the available
records do not establish how this device-level behavior fits the first
usable release or what implementation constraints apply. Keep it in the
backlog and clarify scope rather than assume it is release-critical.

------------------------------------------------------------------------

## Open Questions Carried Forward

-   **Q-01 --- FR-7 progress scope:** Which information must persist
    (for example, activity results, saved problems, or both), and which
    activities are covered? US-06 cannot be finalized until this is
    defined.
-   **Q-02 --- FR-7 retention:** How long must saved progress remain
    available? This affects US-06 acceptance criteria and
    implementation.
-   **Q-03 --- Identity/session approach:** What authentication and
    session behavior will identify the learner across visits? US-06
    depends on this decision.
-   **Q-04 --- Memory Bank capacity:** What should the learner see or be
    able to do when 10 problems are already stored? US-03 needs this
    clarified.
-   **Q-05 --- Activity scope:** Which DataMan activities are included
    in the release? The supplied decision records describe
    prioritization methods but do not specify a DataMan capacity limit
    or final release slice.
-   **Q-06 --- Device inactivity:** Which actions count as "use," and
    what tolerance is acceptable for "approximately five minutes"? US-07
    needs this clarified.
-   **Q-07 --- Manual conflicts:** The requirements notes identify
    unresolved conflicts involving Missing Number, Force Out's starting
    number, Wipe Out behavior after misses, difficulty levels, input
    restrictions, and timer variation. Do not resolve these by
    assumption; keep affected stories out of Move Forward until the
    relevant requirement and source behavior are reconciled.
-   **Q-08 --- DataMan priority/capacity:** The M3 records provide
    useful decision principles but do not specify a DataMan point
    budget. Confirm available capacity before committing to a release
    slice.

## Revisions After Triage and Release Planning

-   **US-01 --- Move Forward:** Immediate answer feedback is ranked
    first because the M3 triage record says it is required for the first
    usable release.
-   **US-02 --- Move Forward with explicit criteria:** The retry story
    is kept near the core answer-checking flow; the two-attempt behavior
    is made observable from FR-2.
-   **US-03 --- Refine:** Storage and feedback are linked to FR-5 and
    FR-6, with the 10-problem constraint from NFR-5 and the unresolved
    full-capacity behavior made visible.
-   **US-06 --- Refine:** Progress preservation remains visible because
    it has high learner value, but it is not treated as ready while the
    identity/session approach and persistence scope are unresolved.
-   **US-07 --- Refine:** The device inactivity behavior is retained,
    but its release priority and exact timing/action semantics require
    clarification.
-   **Priority order is provisional:** The M3 records support
    prioritizing value, risk, readiness, dependencies, and stakeholder
    needs, but they do not establish a DataMan capacity budget. Revisit
    the order after DataMan scope and capacity are confirmed.


