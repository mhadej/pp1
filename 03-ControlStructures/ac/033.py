five = 0
two  = 0
one  = 0

amount = int(input("Enter the amount in PLN: "))
buffer = amount

while amount:
    if amount >= 5 and amount/5 > 0:
        five += 1
        amount -= 5
    elif amount >= 2 and amount/2 > 0:
        two += 1
        amount -= 2
    else:
        one += 1
        amount -= 1

print(f"The amount of PLN {buffer} in coins: \n5zł - {five}\n2zł - {two}\n1zł - {one}")
    