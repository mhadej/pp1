sum      = 0
quantity = 0

while True:
    number = int(input("Enter number: "))
    if number:
        sum += number
        quantity += 1
    else:
        break

print(f"Quantity: {quantity}, Sum = {sum}, Mean = {sum/quantity}")

