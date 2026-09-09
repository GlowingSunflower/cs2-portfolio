validregistration = True

if validregistration:
    
    def validate_name(name):
        if name == "":
            return False, "Student name required."
        return True, name

    def validate_age(age_str):
        try:
            age = int(age_str)
            if 11 <= age <= 18:
                return True, age
            else:
                return False, "Your age must be between 11 and 18 to proceed."
        except ValueError:
            return False, "Please input a valid integer (ex. 12, 15)."

    def validate_grade(grade_str):
        valid_grades = ["7", "8", "9", "10", "11", "12"]
        if grade_str in valid_grades:
            return True, int(grade_str)
        else:
            return False, "Invalid grade level."

    def validate_email(email):
        if "@" in email and "." in email:
            return True, email
        else:
            return False, "Invalid email format. Must contain '@' and '.'."

    def validate_code(code):
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


    # --- ONE BIG IF-ELSE VALIDATION CHAIN ---
    # Running validations sequentially. If one fails, it sets the reason.
    is_valid = True
    error_message = ""

    # 1. Check Name
    success, result = validate_name(input_name)
    if not success:
        is_valid = False
        error_message = result
    else:
        # 2. Check Age
        success, result = validate_age(input_age)
        if not success:
            is_valid = False
            error_message = result
        else:
            # 3. Check Grade Level
            success, result = validate_grade(input_grade)
            if not success:
                is_valid = False
                error_message = result
            else:
                # 4. Check Email
                success, result = validate_email(input_email)
                if not success:
                    is_valid = False
                    error_message = result
                else:
                    # 5. Check Registration Code
                    success, result = validate_code(input_code)
                    if not success:
                        is_valid = False
                        error_message = result

    # --- FINAL OUTPUT PRINTING ---
    if is_valid:
        print("\n------------------------------")
        print("REGISTRATION ACCEPTED")
        print("------------------------------")
        print(f"Student: {input_name}")
        print(f"Age: {input_age}")
        print(f"Grade Level: {input_grade}")
        print(f"Email: {input_email}")
        print(f"Registration Code: {input_code}")
    else:
        print("\n------------------------------")
        print("REGISTRATION NOT ACCEPTED")
        print("------------------------------")
        print(f"Reason: {error_message}")

else:
    print("System offline.")
