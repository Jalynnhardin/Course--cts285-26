# DataMan Requirements Register

## Purpose

This document records the confirmed functional and non-functional requirements identified during Module 2 requirements elicitation.

The requirements are based on two sources of evidence:

1. The DataMan manual, including the Story and Operating Notes.
2. Stakeholder and elicitation information gathered during Module 2.

The requirements describe what the system needs to do or what constraints it must satisfy. Specific implementation choices are not included unless they are supported by the evidence.

---

# Functional Requirements

## FR-1: Check Arithmetic Answers

**Requirement:** The system must allow a learner to enter an arithmetic problem and an answer and indicate whether the answer is correct or incorrect.

**Source/Rationale:** DataMan manual, **Answer Checker (Operating Notes)**. The manual states that the user enters both the problem and answer and that DataMan indicates whether the answer is right or wrong.

**Status:** Confirmed

---

## FR-2: Allow a Second Attempt

**Requirement:** When a learner enters an incorrect answer, the system must allow another attempt before displaying the correct result.

**Source/Rationale:** DataMan manual, **Answer Checker (Story)** and **Answer Checker (Operating Notes)**. The manual describes two tries and states that after two incorrect attempts, DataMan displays the correct result.
**Status:** Confirmed

---

## FR-3: Display Practice Results

**Requirement:** The system must display the number of correct answers and the number of problems attempted after an Answer Checker practice session.

**Source/Rationale:** DataMan manual, **Answer Checker (Operating Notes)**. The manual states that after 10 problems, DataMan displays the number of right answers and the number of problems tried.

**Status:** Confirmed

---

## FR-4: Provide Number Guesser

**Requirement:** The system must provide a Number Guesser activity that selects a secret number, accepts learner guesses, provides information that narrows the possible number, and displays the total number of guesses when the secret number is found.

**Source/Rationale:** DataMan manual, **Number Guesser (Operating Notes)**. The manual states that the secret number is between 9 and 100, that each guess receives a range hint, and that the total number of guesses is displayed when the secret number is found.

**Status:** Confirmed

---

## FR-5: Store Practice Problems

**Requirement:** The system must allow practice problems to be stored for later practice.

**Source/Rationale:** DataMan manual, **Memory Bank (Operating Notes)**. The manual states that problems can be entered and stored and later brought back for practice.

**Status:** Confirmed

---

## FR-6: Provide Feedback During Practice

**Requirement:** The system must indicate whether a learner's answer to a stored practice problem is correct or incorrect.

**Source/Rationale:** DataMan manual, **Memory Bank (Operating Notes)**. The manual states that learners receive right/wrong feedback while practicing stored problems.

**Status:** Confirmed

---

## FR-7: Preserve Saved Practice Progress

**Requirement:** The system must preserve a learner's saved practice progress so that the learner can access that progress when returning in a later authenticated session.

**Source/Rationale:** Module 2 stakeholder elicitation. A stakeholder reported that students lose their practice progress when they leave and return later. The elicitation identified preservation of saved practice progress between authenticated sessions as the underlying need.

**Status:** Confirmed stakeholder requirement

**Clarification Needed:** The exact information that must be preserved and how long it must be retained have not yet been defined.

---

# Non-Functional Requirements

## NFR-1: Problem Input Limit

**Requirement:** The Answer Checker must accept problems containing one- or two-digit numbers.

**Source/Rationale:** DataMan manual, **Answer Checker (Operating Notes)**. The manual states that the Answer Checker accepts problems with one- or two-digit numbers.

**Status:** Confirmed

---

## NFR-2: Answer Input Limit

**Requirement:** The Answer Checker must accept answers containing one, two, or three digits.

**Source/Rationale:** DataMan manual, **Answer Checker (Operating Notes)**. The manual states that answers may contain one, two, or three digits.

**Status:** Confirmed

---

## NFR-3: Negative Results

**Requirement:** The Answer Checker must not accept subtraction problems that result in a negative answer.

**Source/Rationale:** DataMan manual, **Answer Checker (Operating Notes)**. The manual states that DataMan does not handle negative numbers and will not accept subtraction problems that result in a negative answer.

**Status:** Confirmed

---

## NFR-4: Automatic Power Saving

**Requirement:** The system must automatically turn off after approximately five minutes of non-use.

**Source/Rationale:** DataMan manual, **Operating Instructions / POWER SAVER FEATURE**. The manual states that DataMan automatically turns off after about five minutes of non-use to conserve battery power.

**Status:** Confirmed

---

## NFR-5: Memory Bank Capacity

**Requirement:** The Memory Bank must support storage of up to 10 practice problems.

**Source/Rationale:** DataMan manual, **Memory Bank (Operating Notes)**. The manual states that up to 10 problems can be entered and stored.

**Status:** Confirmed

---

# Evidence Notes

## Evidence 1: Answer Checker

The DataMan manual documents the Answer Checker as a practice activity in which the learner enters a problem and answer. DataMan indicates whether the answer is right or wrong. The manual also documents two attempts and the display of the correct answer after two unsuccessful attempts.

**Supports:** FR-1, FR-2, FR-3, NFR-1, NFR-2, NFR-3.

---

## Evidence 2: Practice Scoring

The manual states that after 10 Answer Checker problems, DataMan displays the number of correct answers and the number of problems tried.

**Supports:** FR-3.

---

## Evidence 3: Memory Bank

The manual documents a Memory Bank that can store up to 10 problems for later practice. The stored problems can be presented to the learner, who receives right/wrong feedback and a final score and time.

**Supports:** FR-5, FR-6, NFR-5.

---

## Evidence 4: Number Guesser

The manual documents Number Guesser as an activity involving a secret number between 9 and 100. The learner makes guesses and receives information showing the range in which the secret number lies. When the number is found, the total number of guesses is displayed.

**Supports:** FR-4.

---

## Evidence 5: Power Saver

The manual documents an automatic power-saving behavior. DataMan turns itself off after approximately five minutes without use.

**Supports:** NFR-4.

---

## Evidence 6: Stakeholder Elicitation

During Module 2 elicitation, a stakeholder reported that students lose practice progress when they leave and return later.

The elicitation translated this stakeholder statement into the underlying need for learners to be able to return to previously saved practice progress.

**Supports:** FR-7.

---

# Evidence → Need → Requirement Trace

## Trace: Practice Progress

**Evidence:**
A stakeholder reported that students lose their practice progress when they leave and return later.

**Need:**
Learners need to be able to leave and return to the system without losing previously saved practice progress.

**Requirement:**
**FR-7:** The system must preserve a learner's saved practice progress so that the learner can access that progress when returning in a later authenticated session.

**Remaining Question:**
The project still needs to determine exactly what information counts as saved practice progress and how long it must be retained.

---

# Open Questions

The following items require additional clarification and are not treated as confirmed requirements.

1. What specific practice information must be preserved between authenticated sessions?

2. How long should saved practice progress remain available?

3. Which DataMan activities should save progress?

4. Should Memory Bank problems remain available after a learner leaves and returns?

5. What authentication method will be used to identify a learner?

6. What should happen when the Memory Bank reaches its 10-problem capacity?

7. Which DataMan activities are required in the final system beyond the activities already supported by the current evidence?

8. How should conflicting descriptions in the DataMan manual be resolved when determining the final system behavior?

---

# Assumptions

1. The DataMan manual is being used as evidence of documented behavior. A behavior documented in the manual is not automatically considered a new-project requirement unless it is relevant to the project scope.

2. Stakeholder statements are treated as evidence of stakeholder needs rather than as instructions for a specific technical solution.

3. Specific technologies, databases, programming languages, and interface designs are not requirements unless the project establishes them as constraints.

4. The Memory Bank capacity of 10 problems is treated as a confirmed constraint because it is explicitly documented in the DataMan Operating Notes.

5. The stakeholder requirement concerning saved practice progress is based on Module 2 elicitation evidence rather than on the original DataMan manual.

6. When the Story and Operating Notes contain conflicting information, the conflict is documented rather than silently resolved.

---

# Documentation Conflicts

The DataMan manual states that both the Story and Operating Notes should be consulted because neither section is complete and some information differs between them.

The manual's analyst notes identify several conflicts or omissions, including:

* Differences concerning the Missing Number activity.
* Differences concerning the Force Out starting number.
* Differences concerning Wipe Out behavior after missed answers.
* Differences concerning difficulty levels.
* Input restrictions that appear in the Operating Notes but not necessarily in the Story.
* Timer behavior that can vary based on battery condition and temperature.

These conflicts are recorded as issues requiring analysis rather than being resolved through unsupported assumptions.

---

# Requirement Quality Checks

The requirements in this register are intended to meet the following quality criteria.

### Clear

Each requirement states a specific system behavior, constraint, or operating condition.

### Supported

Each confirmed requirement identifies a source or rationale.

### Testable

The requirement can be checked through testing, inspection, or demonstration.

### Solution-Neutral

The requirements describe what the system needs to accomplish without unnecessarily specifying how the system must be implemented.

### Atomic

Each requirement focuses on one primary capability or constraint where practical.

### Correctly Classified

Functional requirements describe system behavior.

Non-functional requirements describe constraints, operating conditions, or other characteristics governing how the system operates.

### Uncertainty Separated

Open questions and assumptions are listed separately from confirmed requirements so unresolved issues are not presented as established facts.

---

# Source Summary

## DataMan Manual

Primary documented evidence includes:

* Answer Checker
* Memory Bank
* Number Guesser
* Operating Instructions
* Power Saver behavior
* Input limitations
* Practice scoring
* Documented conflicts between the Story and Operating Notes

## Module 2 Stakeholder/Elicitation Evidence

The stakeholder elicitation identified a problem in which students lose practice progress when leaving and returning to the system.

The resulting requirement is:

**FR-7:** The system must preserve a learner's saved practice progress so that the learner can access that progress when returning in a later authenticated session.

Additional details concerning the exact saved information, retention period, authentication, and affected activities remain open questions.
