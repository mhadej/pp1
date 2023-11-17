amount = int(input("Number of products purchased: "))
price  = float(input("Product price: "))

to_pay = 0

if amount > 2:
    to_pay += (amount - 2)*price*0.75
    to_pay += price * 2
else:
    to_pay += amount * price
print(f"Amount to pay: {to_pay}")