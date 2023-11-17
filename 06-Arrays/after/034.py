array = [2, 1, 3, 7, 6, 9, 4, 2, 0]

for i in array:
    if not(i%2):
        print(i, end=" ")

print()

for i in array:
    if i%2:
        print(i, end=" ")
