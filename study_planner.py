import json
sessions = []
def classify_session(duration):
    
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"
    def add_session():
        print ("\n===== ADD STUDY SESSION =====")

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    date = input("Enter date/day: ")

    while True:
        try:
            duration = int(input("Enter duration in minutes: "))

            if duration > 0:
                break
            else:
                print("Duration must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(session)

    print("Study session added successfully!")
    def view_sessions():
        print("\n===== ALL STUDY SESSIONS =====")

    if not sessions:
        print("No study sessions recorded.")
        return

    print("-" * 80)
    print(
        f"{'Subject':<15}"
        f"{'Topic':<20}"
        f"{'Date':<15}"
        f"{'Duration':<12}"
        f"{'Class'}"
    )
    print("-" * 80)

    for session in sessions:
        classification = classify_session(session["duration"])

        print(
            f"{session['subject']:<15}"
            f"{session['topic']:<20}"
            f"{session['date']:<15}"
            f"{session['duration']:<12}"
            f"{classification}"
        )

    print("-" * 80)
    def search_by_subject():
        print("\n===== SEARCH BY SUBJECT =====")

    subject = input("Enter subject to search: ")

    found_sessions = []

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            found_sessions.append(session)

    if not found_sessions:
        print("No sessions found for that subject.")
        return

    total_time = 0

    print(f"\nSessions for {subject}:")
    print("-" * 60)

    for session in found_sessions:
        classification = classify_session(session["duration"])

        print(f"Subject: {session['subject']}")
        print(f"Topic: {session['topic']}")
        print(f"Date: {session['date']}")
        print(f"Duration: {session['duration']} minutes")
        print(f"Classification: {classification}")
        print("-" * 60)

        total_time += session["duration"]

    print(f"Total time spent on {subject}: {total_time} minutes")
    def study_statistics():
        print("\n===== STUDY STATISTICS =====")

    if not sessions:
        print("No study sessions available.")
        return

    total_minutes = sum(session["duration"] for session in sessions)

    subject_totals = {}

    for session in sessions:
        subject = session["subject"]

        if subject not in subject_totals:
            subject_totals[subject] = 0

        subject_totals[subject] += session["duration"]

    weakest_subject = min(subject_totals, key=subject_totals.get)

    longest_session = max(
        sessions,
        key=lambda session: session["duration"]
    )

    print(f"Total hours studied: {total_minutes / 60:.2f} hours")

    print("\nTotal time per subject:")

    for subject, minutes in subject_totals.items():
        print(f"{subject}: {minutes} minutes")

    print(
        f"\nSubject with least study time: "
        f"{weakest_subject} "
        f"({subject_totals[weakest_subject]} minutes)"
    )

    print(
        f"Longest study session: "
        f"{longest_session['subject']} - "
        f"{longest_session['topic']} "
        f"({longest_session['duration']} minutes)"
    )
    def save_sessions():
        try:
            with open("study_log.txt", "w") as file:
                json.dump(sessions, file, indent=4)

            print("Study sessions saved successfully.")

        except Exception as error:
            print("Error saving sessions:", error)
            def load_sessions():
                global sessions

    try:
        with open("study_log.txt", "r") as file:
            sessions = json.load(file)

        print("Previous study sessions loaded successfully.")

    except FileNotFoundError:
        sessions = []
        print("No previous study file found. Starting with an empty list.")

    except json.JSONDecodeError:
        sessions = []
        print("Study file is invalid. Starting with an empty list.")

print("Welcome to Smart Study Planner!")

def main():
    load_sessions()

    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View study statistics")
        print("5. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sessions()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            search_by_subject()
        elif choice == "4":
            study_statistics()
        elif choice == "5":
            print("Saving and exiting...")
            break
def load_sessions():
    global sessions

    try:
        with open("study_log.txt", "r") as file:
            sessions = json.load(file)

    except FileNotFoundError:
        sessions = []

def add_sessions():
    print("===== ADD STUDY SESSION =====")

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    date = input("Enter date/day: ")
    duration = int(input("Enter duration in minutes: "))

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(session)

    print("Study session added successfully!")

def view_sessions():
    print("===== ALL STUDY SESSIONS =====")

    if not sessions:
        print("No study sessions recorded.")
        return

    for session in sessions:
        print("--------------------")
        print("Subject:", session["subject"])
        print("Topic:", session["topic"])
        print("Date:", session["date"])
        print("Duration:", session["duration"], "minutes")
        print("Classification:", classify_session(session["duration"]))

def search_by_subject():
    subject = input("Enter subject to search: ")

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            print("--------------------")
            print("Subject:", session["subject"])
            print("Topic:", session["topic"])
            print("Date:", session["date"])
            print("Duration:", session["duration"], "minutes")
            print("Classification:", classify_session(session["duration"]))

def study_statistics():
    if not sessions:
        print("No study sessions available.")
        return

    total_minutes = sum(session["duration"] for session in sessions)

    print("Total hours studied:", total_minutes / 60)

    subject_totals = {}

    for session in sessions:
        subject = session["subject"]

        if subject not in subject_totals:
            subject_totals[subject] = 0

        subject_totals[subject] += session["duration"]

    print("Total time per subject:")

    for subject, minutes in subject_totals.items():
        print(subject, ":", minutes, "minutes")

    least_subject = min(subject_totals, key=subject_totals.get)

    print("Subject with least study time:", least_subject)

    longest = max(sessions, key=lambda session: session["duration"])

    print(
        "Longest study session:",
        longest["subject"],
        "-",
        longest["topic"],
        longest["duration"],
        "minutes"
    )
if __name__ == "__main__":
    main()

