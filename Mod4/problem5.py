'''
#5. A store charges $5 for shipping on any order under $50.
If the order amount is $50 or more, shipping is free. 
Ask the user for the order total and print the total cost, including shipping.
'''

order_amount = float(input("What is your order amount? "))
if (order_amount < 50):
  order_amount += 5

print("The total cost of your order, including shipping, is $", order_amount)
