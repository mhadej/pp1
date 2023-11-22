file = open(r'during/numbers.txt')

sum = 0

for i in file:
    sum += int(i)

print(sum)
file.close()