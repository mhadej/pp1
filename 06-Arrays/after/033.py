array = [2, 1, 3, 7]

your_nr = int(input("Enter a number: "))

sum = 0

for i in array:
    if i > your_nr:
        sum += 1

print(sum)