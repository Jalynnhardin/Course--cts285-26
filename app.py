"""Text-only interface for the DataMan Memory Bank prototype."""
from dataman import logic, store


def show_problems(problems):
    if not problems:
        print("No problems are available.")
        return
    for problem in problems:
        print(f"{problem['id']}: {problem['question']}")


def create_practice_set(data):
    name = input("Enter a name for the practice set: ").strip()
    if not name:
        print("Practice set name cannot be blank.")
        return
    practice_set = logic.create_practice_set(data, name)
    store.save_data(data)
    print(f"Created practice set {practice_set['id']}: {practice_set['name']}")


def add_problem(data):
    if not data["practice_sets"]:
        print("Create a practice set first.")
        return
    for item in data["practice_sets"]:
        print(f"{item['id']}: {item['name']} ({len(item['problem_ids'])}/10 problems)")
    set_id = input("Enter the practice set ID: ").strip()
    practice_set = logic.find_practice_set(data, set_id)
    if practice_set is None:
        print("Practice set not found.")
        return

    problem_id = input("Enter a problem ID (for example P6): ").strip().upper()
    question = input("Enter the problem: ").strip()
    answer_text = input("Enter the correct answer: ").strip()
    if not problem_id or not question or not answer_text:
        print("Problem ID, question, and answer are required.")
        return
    try:
        answer = int(answer_text)
        logic.add_problem(data, set_id, problem_id, question, answer)
        store.save_data(data)
        print("Problem added.")
    except (ValueError, KeyError) as error:
        print(f"Could not add problem: {error}")


def practice(data):
    if not data["practice_sets"]:
        print("There are no practice sets yet.")
        return
    for item in data["practice_sets"]:
        print(f"{item['id']}: {item['name']}")
    set_id = input("Enter the practice set ID: ").strip()
    practice_set = logic.find_practice_set(data, set_id)
    if practice_set is None:
        print("Practice set not found.")
        return
    problems = logic.get_set_problems(data, set_id)
    if not problems:
        print("This practice set has no problems.")
        return

    learner = input("Enter learner name: ").strip()
    if not learner:
        print("Learner name cannot be blank.")
        return
    session_id = logic.start_session(data, learner, set_id)
    store.save_data(data)
    print(f"\nStarting practice session {session_id}. You have two attempts per problem.")

    for problem in problems:
        print(f"\n{problem['id']}: {problem['question']}")
        try_number = 1
        while try_number <= logic.MAX_ATTEMPTS:
            answer_text = input(f"Attempt {try_number} - your answer: ").strip()
            try:
                answer = int(answer_text)
            except ValueError:
                print("Please enter a whole number. This does not count as an attempt.")
                continue

            outcome = logic.record_attempt(
                data, session_id, problem["id"], try_number, answer
            )
            store.save_data(data)
            if outcome["correct"]:
                print("Correct!")
                break
            if try_number == 1:
                print("Not quite. Try once more. The correct answer is still hidden.")
            else:
                print(f"Two incorrect attempts. The correct answer is {problem['answer']}.")
            try_number += 1

    summary = logic.finish_session(data, session_id)
    store.save_data(data)
    print("\nPractice session complete.")
    print(f"Correct on first attempt: {summary['first_try_correct']}")
    print(f"Correct on second attempt: {summary['second_try_correct']}")
    print(f"Missed (two incorrect attempts): {summary['missed']}")


def curator_report(data):
    if not data["sessions"]:
        print("No completed practice sessions are available.")
        return
    for session in data["sessions"]:
        print(
            f"{session['id']}: {session['learner']} - "
            f"{session['practice_set_id']} - {session.get('status', 'in progress')}"
        )
    session_id = input("Enter the session ID to retrieve: ").strip()
    try:
        report = logic.get_curator_report(data, session_id)
    except KeyError:
        print("Session not found.")
        return

    print(f"\nCurator report for {report['learner']}")
    print(f"Practice set: {report['practice_set_id']}")
    print(f"First-try successes: {len(report['first_try_successes'])}")
    print(f"Second-try successes: {len(report['second_try_successes'])}")
    print(f"Missed problems: {len(report['missed_problems'])}")

    for heading, key in (
        ("First-try successes", "first_try_successes"),
        ("Second-try successes", "second_try_successes"),
        ("Missed problems", "missed_problems"),
    ):
        print(f"\n{heading}:")
        if not report[key]:
            print("  None")
        for item in report[key]:
            print(f"  {item['problem_id']}: {item['question']}")


def main():
    data = store.load_data()
    while True:
        print("\n===== DATAMAN MEMORY BANK =====")
        print("1. Create a practice set")
        print("2. Add a problem to a practice set")
        print("3. Learner practice")
        print("4. Curator: retrieve session results and missed problems")
        print("5. List practice sets and problems")
        print("0. Save and exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_practice_set(data)
        elif choice == "2":
            add_problem(data)
        elif choice == "3":
            practice(data)
        elif choice == "4":
            curator_report(data)
        elif choice == "5":
            for item in data["practice_sets"]:
                print(f"\n{item['id']}: {item['name']}")
                show_problems(logic.get_set_problems(data, item["id"]))
        elif choice == "0":
            store.save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0 through 5.")


if __name__ == "__main__":
    main()
