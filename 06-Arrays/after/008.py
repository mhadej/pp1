array = [15, 8, 31, 47, 2, 19]
i = int(len(array)-1)
sum = 0

while i>=0:
    sum += array[i]
    i -= 1

print(f"{array}, mean: {sum/len(array)}")