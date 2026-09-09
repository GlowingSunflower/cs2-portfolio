while True:
  name = input("Please enter student name: ")
  if name == "":
    print("Student name required.")
  else:
    break

while True:
    try:
      age = int(input("Please enter your age: ")) 
      if 11 <= age <= 18:
        break 
      else:
        print("Your age must be between 11 and 18 to proceed.")
            
    except ValueError:
          print("Please input a valid integer (ex. 12, 15,,). ")


print("\n ------------------------------", "\n REGISTRATION ACCEPTED", "\n ------------------------------" )
