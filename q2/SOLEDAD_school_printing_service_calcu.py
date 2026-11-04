#School Printing Service Calculator

def calculate_printing_cost(pages, price_per_page):
  return pages * price_per_page
  
def calculate_balance(payment, total_cost):
  if payment >= total_cost:
      return payment - total_cost
  else:
      return total_cost - payment

pages = int(input("Please enter number of pages to print: "))
price_per_page = 3.00
payment = float(input("Please enter amount paid: "))

total_cost = calculate_printing_cost(pages, price_per_page)

print(f"Total Cost: PHP {total_cost:.2f}")

if payment >= total_cost:
    print(f"Change: PHP {calculate_balance(payment, total_cost):.2f}")
else:
    print(f"Additional Amount Needed: PHP {calculate_balance(payment, total_cost):.2f}")
