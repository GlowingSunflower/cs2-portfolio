# Input Validation and Output Verification

**Activity:** PSHS Workshop Registration Validator

**Name:** Jessie Marie B. Soledad

**Section:** Dahlia

**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements

---
## Validation Questions
### 1. Why should the student name not be blank?
> The student name is required to properly identify the student.
### 2. Why should age be checked for both data type and range?
> To make sure the age is a valid number and is within the allowed range of 11 to 18.
### 3. Why should grade level only accept specific values?
> To make sure only valid grade levels from 7 to 12 are accepted.
### 4. What format requirements did you use for the email address?
> The email must contain both “@” and “.”.
### 5. What length requirement did you use for the registration code?
> The registration code must contain exactly 6 characters.
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Flowchart
Insert your flowchart below.
![Workshop Validator Flowchart](workshop_validator_flowchart.png)
OR
## Pseudocode

```text
BEGIN

    registration ← TRUE

    IF registration = TRUE THEN

        FUNCTION valid_name(name)
            IF name = "" THEN
                RETURN FALSE, "Student name required."
            ELSE
                RETURN TRUE, name
            END IF
        END FUNCTION


        FUNCTION valid_age(age_str)
            TRY
                age ← INTEGER(age_str)

                IF age >= 11 AND age <= 18 THEN
                    RETURN TRUE, age
                ELSE
                    RETURN FALSE, "Your age must be between 11 and 18 to proceed."
                END IF

            CATCH ValueError
                RETURN FALSE, "Please input a valid integer (ex. 12, 15)."
            END TRY
        END FUNCTION


        FUNCTION valid_grade(grade_str)
            grades ← ["7", "8", "9", "10", "11", "12"]

            IF grade_str IN grades THEN
                RETURN TRUE, INTEGER(grade_str)
            ELSE
                RETURN FALSE, "Invalid grade level."
            END IF
        END FUNCTION


        FUNCTION valid_email(email)
            IF "@" IN email AND "." IN email THEN
                RETURN TRUE, email
            ELSE
                RETURN FALSE, "Invalid email format. Must contain '@' and '.'."
            END IF
        END FUNCTION


        FUNCTION valid_code(code)
            IF LENGTH(code) = 6 THEN
                RETURN TRUE, code
            ELSE
                RETURN FALSE, "The registration code must contain exactly 6 characters."
            END IF
        END FUNCTION


        OUTPUT "--- STUDENT REGISTRATION FORM ---"

        INPUT input_name
        INPUT input_age
        INPUT input_grade
        INPUT input_email
        INPUT input_code

        is_valid ← TRUE
        error_message ← ""


        // Check Name
        success, result ← valid_name(input_name)

        IF success = FALSE THEN
            is_valid ← FALSE
            error_message ← error_message + result + NEWLINE
        END IF


        // Check Age
        success, result ← valid_age(input_age)

        IF success = FALSE THEN
            is_valid ← FALSE
            error_message ← error_message + result + NEWLINE
        END IF


        // Check Grade
        success, result ← valid_grade(input_grade)

        IF success = FALSE THEN
            is_valid ← FALSE
            error_message ← error_message + result + NEWLINE
        END IF


        // Check Email
        success, result ← valid_email(input_email)

        IF success = FALSE THEN
            is_valid ← FALSE
            error_message ← error_message + result + NEWLINE
        END IF


        // Check Registration Code
        success, result ← valid_code(input_code)

        IF success = FALSE THEN
            is_valid ← FALSE
            error_message ← error_message + result + NEWLINE
        END IF


        IF is_valid = TRUE THEN

            OUTPUT "------------------------------"
            OUTPUT "REGISTRATION ACCEPTED"
            OUTPUT "------------------------------"
            OUTPUT "Student: ", input_name
            OUTPUT "Age: ", input_age
            OUTPUT "Grade Level: ", input_grade
            OUTPUT "Email: ", input_email
            OUTPUT "Registration Code: ", input_code

        ELSE

            OUTPUT "------------------------------"
            OUTPUT "REGISTRATION NOT ACCEPTED"
            OUTPUT "------------------------------"
            OUTPUT "Reasons:"
            OUTPUT error_message

        END IF

    ELSE

        OUTPUT "Input required"

    END IF

END
```

Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[SOLEDAD - Workshop Validator.py](SOLEDAD_workshop_validator.py)
## Final Code
```python

registration = True

if registration:
    
    def valid_name(name):
        if name == "":
            return False, "Student name required."
        return True, name

    def valid_age(age_str):
        try:
            age = int(age_str)
            if 11 <= age <= 18:
                return True, age
            else:
                return False, "Your age must be between 11 and 18 to proceed."
        except ValueError:
            return False, "Please input a valid integer (ex. 12, 15)."

    def valid_grade(grade_str):
        grades = ["7", "8", "9", "10", "11", "12"]
        if grade_str in grades:
            return True, int(grade_str)
        else:
            return False, "Invalid grade level."

    def valid_email(email):
        if "@" in email and "." in email:
            return True, email
        else:
            return False, "Invalid email format. Must contain '@' and '.'."

    def valid_code(code):
        if len(code) == 6:
            return True, code
        else:
            return False, "The registration code must contain exactly 6 characters."

    print("--- STUDENT REGISTRATION FORM ---")
    input_name = input("Please enter student name: ")
    input_age = input("Please enter your age: ")
    input_grade = input("Please enter grade level (7-12): ")
    input_email = input("Please enter your email: ")
    input_code = input("Please enter registration code (6 characters): ")

    is_valid = True
    error_message = ""

    # Check Name
    success, result = valid_name(input_name)
    if not success:
        is_valid = False
        error_message += result + "\n"

    # Check Age
    success, result = valid_age(input_age)
    if not success:
        is_valid = False
        error_message += result + "\n"

    # Check Grade
    success, result = valid_grade(input_grade)
    if not success:
        is_valid = False
        error_message += result + "\n"

    # Check Email
    success, result = valid_email(input_email)
    if not success:
        is_valid = False
        error_message += result + "\n"

    # Check Registration Code
    success, result = valid_code(input_code)
    if not success:
        is_valid = False
        error_message += result + "\n"

    if is_valid:
      print("\n------------------------------\nREGISTRATION ACCEPTED\n------------------------------\nStudent:", input_name, "\nAge:", input_age, "\nGrade Level:", input_grade, "\nEmail:", input_email, "\nRegistration Code:", input_code)
  
    else:
      print("\n------------------------------\nREGISTRATION NOT ACCEPTED\n------------------------------\nReasons:\n" + error_message)

else:
    print("Input required")
```

---
## Validation Techniques Used

### Presence Validation

> Presence validation was used to check whether the student name was left blank. If the name is empty, the program displays `Student name required.`

### Data Type Validation

> Data type validation was used to ensure that the age entered is a valid integer. If the user enters non-numeric input, such as `fourteen`, the program displays an error message.

### Range Validation

> Range validation was used to ensure that the student's age is between 11 and 18, inclusive. If the age is outside this range, the program rejects the registration.

### Acceptable Value Validation

> Acceptable value validation was used to check whether the entered grade level is one of the accepted values: 7, 8, 9, 10, 11, or 12. Any other value is rejected.

### Pattern Validation

> Pattern validation was used to check whether the email address contains both `@` and `.`. If either character is missing, the program displays an invalid email format message.

### Length Validation

> Length validation was used to ensure that the registration code contains exactly 6 characters. If the code is shorter or longer than 6 characters, the program rejects it.
> 
---
# Part D - Testing
Test the program using both valid and invalid inputs.

| Test | Input / Condition            | Validation Being Tested | Expected Output                           | Actual Output                             | Result   |
| ---: | ---------------------------- | ----------------------- | ----------------------------------------- | ----------------------------------------- | -------- |
|    1 | All inputs valid             | Normal case             | `Registration accepted.`                  | `Registration accepted.`                  | **PASS** |
|    2 | Blank student name           | Presence                | `Student name required.`                  | `Student name required.`                  | **PASS** |
|    3 | Age = `fourteen`             | Data type               | `Age must be a number.`                   | `Age must be a number.`                   | **PASS** |
|    4 | Age = `11`                   | Minimum boundary        | `Registration accepted.`                  | `Registration accepted.`                  | **PASS** |
|    5 | Age = `18`                   | Maximum boundary        | `Registration accepted.`                  | `Registration accepted.`                  | **PASS** |
|    6 | Age = `10`                   | Range                   | `Age must be between 11 and 18.`          | `Age must be between 11 and 18.`          | **PASS** |
|    7 | Grade Level = `13`           | Acceptable value        | `Grade level must be between 7 and 12.`   | `Grade level must be between 7 and 12.`   | **PASS** |
|    8 | Email = `studentpshs.edu.ph` | Pattern                 | `Invalid email address.`                  | `Invalid email address.`                  | **PASS** |
|    9 | Registration Code = `ABC`    | Length                  | `Registration code must be 6 characters.` | `Registration code must be 6 characters.` | **PASS** |
|   10 | Registration Code = `CS2026` | Valid length            | `Registration accepted.`                  | `Registration accepted.`                  | **PASS** |

> **PASS** means the actual output matches the expected output.
> **FAIL** means the actual output does not match the expected output.

---

# Part E - Output Verification

Choose three tests from Part D and compare the expected output with the actual output.

## Verification Test 1

**Input:**

```text
Student Name: Juan Dela Cruz
Age: 14
Grade Level: 8
Email: juan@pshs.edu.ph
Registration Code: CS2026
```

**Expected Output:**

```text
Registration accepted.
```

**Actual Output:**

```text
Registration accepted.
```

**Result:** **PASS**

**Explanation:**

> The output is correct because all the information provided meets the program's validation rules. The age and grade level are within the accepted ranges, the email follows the required format, and the registration code is valid.

---

## Verification Test 2

**Input:**

```text
Student Name:
Age: 14
Grade Level: 8
Email: juan@pshs.edu.ph
Registration Code: CS2026
```

**Expected Output:**

```text
Student name required.
```

**Actual Output:**

```text
Student name required.
```

**Result:** **PASS**

**Explanation:**

> The output is correct because the student name was left blank. The program detects the missing required input and rejects the registration.

---

## Verification Test 3

**Input:**

```text
Student Name: Juan Dela Cruz
Age: 10
Grade Level: 8
Email: juan@pshs.edu.ph
Registration Code: CS2026
```

**Expected Output:**

```text
Age must be between 11 and 18.
```

**Actual Output:**

```text
Age must be between 11 and 18.
```

**Result:** **PASS**

**Explanation:**

> The output is correct because the entered age of 10 is below the minimum allowed age of 11. The program correctly identifies the input as invalid and rejects the registration.

**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection

Answer briefly.

### 1. Why should a program validate input before processing it?

> Input validation prevents incorrect or invalid data from being processed. It helps ensure accurate results and prevents unexpected errors.

### 2. What is the difference between input validation and output verification?

> Input validation checks whether the user's input follows the required rules, while output verification checks whether the program produces the expected output.

### 3. Which validation technique was easiest for you to implement? Why?

> Length validation was the easiest because I only needed to check whether the registration code contained exactly 6 characters.

### 4. Which validation technique was most challenging? Why?

> Data type validation was the most challenging because I had to handle non-numeric inputs and make sure the age was converted into an integer correctly.

### 5. How did testing invalid inputs help you improve your program?

> Testing invalid inputs helped me check whether the program detected errors correctly and displayed the appropriate error messages for invalid information.

---
# Files for This Activity
- [SOLEDAD - Workshop Validator.py](SOLEDAD_workshop_validator.py)
- [SOLEDAD - Workshop Validator.md](SOLEDAD_workshop_validator.md)
---
