VALID_SECTIONS = ["Dahlia", "Ilang-Ilang", "Rosal", "Sampaguita"]
VALID_CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]
VALID_ATTENDANCE = ["Present", "Absent", "Late"]


def validate_email(email):
    # Simple activity-level check: @ and a period after @.
    return "@" in email and "." in email.split("@", 1)[1]


def main():
    # Collect only the five required fields.
    student_name = input("Student Name: ").strip()
    section = input("Section: ").strip()
    club_choice = input("Club Choice: ").strip()
    school_email = input("School Email: ").strip()
    attendance_status = input("Attendance Status: ").strip()

    errors = []

    if not student_name:
        errors.append("Student name is required.")

    if section not in VALID_SECTIONS:
        errors.append("Please choose a valid section.")

    if club_choice not in VALID_CLUBS:
        errors.append("Please choose a valid club.")

    if not validate_email(school_email):
        errors.append(
            "Please enter a valid school email containing @ "
            "and a period after @."
        )

    if attendance_status not in VALID_ATTENDANCE:
        errors.append("Please choose a valid attendance status.")

    # Reject the registration if any field fails validation.
    if errors:
        print("\nREGISTRATION REJECTED")
        for error in errors:
            print(error)
        return

    print("\n--------------------------------")
    print("REGISTRATION ACCEPTED")
    print("--------------------------------")
    print(f"Student: {student_name}")
    print(f"Section: {section}")
    print(f"Club: {club_choice}")
    print(f"Email: {school_email}")
    print(f"Attendance: {attendance_status}")


if __name__ == "__main__":
    main()
