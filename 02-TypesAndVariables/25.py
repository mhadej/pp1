import random

sum = 0

for x in range(3):
    y = random.randint(1,6)
    print(y)
    sum += y
print("Sum: ", sum)