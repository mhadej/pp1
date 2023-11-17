import random

array = [random.randint(1, 999) for i in range(8)]

length = 0

for i in array:
    length += len(str(i))

print("-"*(2*(length+1)))
print("| ", end="")

for i in array:
    print(i, end=" | ")

print()
print("-"*(2*(length+1)))