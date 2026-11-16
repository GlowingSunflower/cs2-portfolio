def show_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

try:
    num = int(input("Please enter a number to generate multiplication table: "))
    show_table(num)
except ValueError:
    print("Invalid input. Please enter an integer.")

# The first part creates a function called show_table that will generate a multiplication table using the number given by the user.
# range(1, 11) gives numbers from 1 to 10. The loop repeats, increasing i by 1 each time.
# The code multiplies the number entered by the user by the current value of i, then prints the equation and answer. This repeats until i reaches 10.
# The try block tells Python to attempt running the code. If an error happens, it will proceed to the except block.
# The program asks the user to enter a number. int() converts the input into a whole number and stores it in num.
# The show_table(num) calls the function and passes the entered number so it can generate the multiplication table.
# If the user enters something that cannot be converted into an integer, a ValueError occurs, and the program skips to the except block.
# The except block prints an error message telling the user to enter a valid whole number instead.
