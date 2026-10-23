**Activity:** PSHS Secure Club Registration System  
**Name:** Jessie Marie B. Soledad
**Section:** Dahlia  
**Quarter:** 1

---

## Activity Overview

> In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple PSHS Club Registration System. The goal is to collect only necessary information and accept only correct, expected input.

---

# Part A - Cybersecurity Threat Analysis

## Assigned Case

**Case Number:** 1  
**Case Title:** Fake Login Alert

> A message claims that a student's account will be disabled and asks them to click a link and enter their username and password.

### 1. What cybersecurity threat is shown?

> The threat is **phishing**, an attempt to trick someone into revealing sensitive information through a fake message or website.

### 2. What warning signs make the situation suspicious?

> The message creates urgency by saying the account will be disabled. It asks the student to click a link and enter login credentials, and the link may lead to a fake website that imitates the school's login page.

### 3. What may be affected?

- **Data:** Login credentials and personal information could be exposed.
- **Account:** Someone could use stolen credentials to access the student's account.
- **Application or device:** A malicious link could expose the user to additional risks.

The main risks are account compromise and misuse of personal data.

### 4. What information could be exposed or misused?

> The student's username, password, school email, and information accessible through the compromised account could be exposed or misused.

### 5. What should the user do to reduce the risk?

> The student should not click the link or enter credentials. They should verify the warning through an official school channel and report the message to a teacher or school IT staff. If they already entered a password, they should contact school IT staff and change it through the official website.

### Mitigation

> Use trusted official websites, check suspicious messages carefully, keep devices and applications updated, and enable multi-factor authentication when available.

---

# Part B - Data Privacy and Secure Data Capture

| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | COLLECT | Identifies the student registering. |
| Section | COLLECT | Identifies the student's class section. |
| Club Choice | COLLECT | Records the club the student wants to join. |
| School Email | COLLECT | Provides a school-related contact method. |
| Attendance Status | COLLECT | Records whether the student is present, absent, or late. |
| Password | DO NOT COLLECT | A club registration form does not need the student's password. |
| OTP | DO NOT COLLECT | An OTP is an authentication secret and is unnecessary for registration. |
| Home Address | DO NOT COLLECT | The home address is not needed for this activity. |
| Parent Bank Account | DO NOT COLLECT | Banking information is unrelated to club registration and is sensitive. |

## Privacy Question

**Why is it safer to collect only information that the program actually needs?**

> Collecting only necessary information reduces the amount of sensitive data that could be exposed, stolen, or misused if the system is compromised. It also respects students' privacy.

---

# Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | At least one non-space character | Incomplete registration | Blank or spaces only | Strip surrounding spaces and reject an empty result | `Student name is required.` |
| Section | Dahlia, Ilang-Ilang, Rosal, or Sampaguita | Incorrect section record | `Orchid` | Accept only an approved section | `Please choose a valid section.` |
| Club Choice | Robotics, Science, Mathematics, or Programming | Unsupported club registration | `Gaming` | Accept only an approved club | `Please choose a valid club.` |
| School Email | Contains `@` and a period after `@` | Incorrect contact information | `studentpshs.edu.ph` or `student@pshs` | Require `@` and a `.` after `@` | `Please enter a valid school email containing @ and a period after @.` |
| Attendance Status | Present, Absent, or Late | Incorrect attendance record | `Excused` | Accept only an approved status | `Please choose a valid attendance status.` |

## Secure Data Capture Questions

### 1. What should your program accept?

> It should accept a nonblank name, an approved section, one of the four listed clubs, a school email containing `@` and a period after `@`, and an approved attendance status.

### 2. What should your program reject?

> It should reject blank names, unapproved sections or clubs, emails that fail the required format check, and attendance statuses other than Present, Absent, or Late.

### 3. How do your validation rules help reduce incorrect or unsafe input?

> Validation rules prevent incomplete or unexpected values from being accepted as valid registrations. They also make errors easier to identify and correct.

---

# Part D - Secure Program Implementation

## Program

The system collects only Student Name, Section, Club Choice, School Email, and Attendance Status. It does not request passwords, OTPs, home addresses, or banking information.

## Source Code File

[`SOLEDAD - Secure Registration.py`](SOLEDAD_secure_registration.py)

## Final Code

```python
# PSHS Secure Club Registration System
# Collect only information needed for club registration.

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
```

## Security Practices Applied

### Required Input

> I used `.strip()` and checked whether the student name was empty. This rejects a blank or spaces-only name.

### Allowed Values

> The approved sections, clubs, and attendance statuses are stored in lists. The program rejects values that are not in the corresponding list.

### Format Check

> The program checks for `@` and a period after `@`. This is a simple activity-level format check, not proof that an email address exists.

### Error Messages

> The program displays a clear error for each invalid field. If any field is invalid, the registration is rejected.

### Data Minimization

> I did not request passwords, OTPs, home addresses, or parent banking information because they are unnecessary for club registration. Collecting less sensitive information reduces privacy and security risks.

---

# Part E - Testing and Reflection

## Testing

Run each test, record the actual output you observe, and mark **PASS** if it matches the expected result or **FAIL** if it does not.

| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | Ana Cruz, Dahlia, Programming, `ana@pshs.edu.ph`, Present | `REGISTRATION ACCEPTED` with all five details | Fill in after running | Fill in |
| 2 | Blank name or spaces only | `REGISTRATION REJECTED` and `Student name is required.` | Fill in after running | Fill in |
| 3 | Section is `Orchid` | `REGISTRATION REJECTED` and `Please choose a valid section.` | Fill in after running | Fill in |
| 4 | Club is `Gaming` | `REGISTRATION REJECTED` and `Please choose a valid club.` | Fill in after running | Fill in |
| 5 | Email is `studentpshs.edu.ph` | `REGISTRATION REJECTED` with the email format error | Fill in after running | Fill in |
| 6 | Email is `student@pshs` | `REGISTRATION REJECTED` with the email format error | Fill in after running | Fill in |
| 7 | Attendance is `Excused` | `REGISTRATION REJECTED` and `Please choose a valid attendance status.` | Fill in after running | Fill in |
| 8 | Maria Santos, Rosal, Science, `maria@pshs.edu.ph`, Late | `REGISTRATION ACCEPTED` with the new details | Fill in after running | Fill in |

## Reflection

### 1. What is one cybersecurity threat that can affect an application or user?

> Phishing tricks users into revealing sensitive information through fake messages or websites.

### 2. How can users reduce the risk of phishing or suspicious messages?

> Users should avoid suspicious links, verify messages through official channels, report suspicious messages, and never share passwords or OTPs in response to unexpected requests.

### 3. How can validation rules improve the security of user input?

> Validation rules reject missing or unexpected values, helping prevent incorrect data from being accepted as a valid registration.

### 4. Why should a program avoid collecting unnecessary personal information?

> Less collected data means less sensitive information could be exposed or misused if a system is compromised.

### 5. How did SG7's input validation concepts become security practices in SG8?

> SG7's input validation concepts became security practices in SG8 by checking required fields, approved values, and input formats before accepting a registration. These checks improve data quality and reduce avoidable errors and risks.

---

# Files for This Activity

- [`SOLEDAD - Secure Registration.py`](SOLEDAD_secure_registration.py)
- [`SOLEDAD - Secure Registration.md`](SOLEDAD_secure_registration.md)

---

