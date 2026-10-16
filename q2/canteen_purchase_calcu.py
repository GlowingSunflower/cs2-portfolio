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
