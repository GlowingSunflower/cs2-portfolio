# Ask the user to enter a student score.student_score = int(input("Please enter your score, dear user: "))
student_score = int(input("Please enter your score, dear user: "))

# Confirm that the score is within the allowed range of 0 to 100.
if student_score < 0 or student_score > 100:
    print("Invalid Score.")
  
elif student_score >= 90:
    print("Your score is Outstanding!")
elif student_score >= 80:
    print("Your score is Very Satisfactory.")
elif student_score >= 75:
    print("Your score is Satisfactory.")
else:
    print("Needs Improvement")
