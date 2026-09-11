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
START
Write your pseudocode here.
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
> Write the programming language used.
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
# Paste your final code here.
```

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> Write your answer here.
### Data Type Validation
Explain where you used data type validation.
> Write your answer here.
### Range Validation
Explain where you used range validation.
> Write your answer here.

### Acceptable Value Validation
Explain where you used acceptable value validation.
> Write your answer here.
### Pattern Validation
Explain the simple pattern rule you used.
> Write your answer here.
### Length Validation
Explain the length rule you used.
> Write your answer here.
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
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used
---
