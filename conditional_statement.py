"""
if/else
if/elif/elif/else
"""

x = 10
if (x == 10):
    print("x is 10")
elif(x == 11):
    print("x is 11")
elif(x == 12):
    print("x is 12")
else:
    print("x is something")

price = int(input("Enter the price: "))
qty = int(input("Enter the quantity: "))
amt = price * qty

if (amt > 1000):
    print("Your can get 20% discount!")
    discount = amt/100*20
    amt = amt - discount
    print("Your payable amount is", amt)
elif (amt == 1000):
    print("You can get 10% discount!")
    discount = amt/100*10
    amt = amt - discount
    print("Your payable amount is", amt)
else:
    print("Your payment is", amt)

marks = int(input("Enter your marks: "))
if marks < 40:
    print("Failed")
elif marks >= 40 and marks< 60:
    print("Passed")
elif (marks >= 60 and marks< 80):
    print("Credit")
elif marks >=80 and marks<=100:
    print("Distinction")
else: 
    print("Out of range.")