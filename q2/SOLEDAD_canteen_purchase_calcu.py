def calculate_total(price, quantity):
  return price * quantity

def calculate_change(payment, total):
  if payment >= total:
      return payment - total
  else:
      return total - payment

price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

total = calculate_total(price, quantity)
change = calculate_change(payment, total)

# Pass the actual arguments price and quantity to the function.
# Store the returned total in the variable total.
total = calculate_total(price, quantity)

# Reuse the stored total and pass it with payment to the function.
change = calculate_change(payment, total)

# Display the results
print(f"Total Cost: PHP {total:.2f}")

# Display change if payment is sufficient; otherwise, show the shortage.
if payment >= total:
    print(f"Change: PHP {change:.2f}")
else:
    print(f"Additional Amount Needed: PHP {change:.2f}")


# DOCUMENTATION QUESTIONS
#
# 1. What does each function do?
# calculate_total() multiplies the item price by the quantity
# and returns the total purchase cost.
# calculate_change() calculates the change if payment is sufficient
# or the shortage if payment is insufficient.
#
# 2. What is the difference between parameters and actual arguments?
# Parameters are the variables listed in a function definition,
# such as price and quantity in calculate_total().
# Actual arguments are the values or variables passed when calling
# the function, such as price and quantity in
# calculate_total(price, quantity).
#
# 3. Where is the returned total stored, and how is it reused?
# The returned total is stored in the variable total.
# It is reused as an argument in calculate_change(payment, total)
# and displayed as the total purchase cost.
#
# 4. Why separate total calculation from change calculation?
# Separating the functions makes the program easier to read, test,
# debug, and reuse because each function has one specific task.
