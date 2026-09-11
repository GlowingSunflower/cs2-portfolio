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
