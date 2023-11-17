array = [2, 3, 7, 5, 4]

print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1])
print(array[len(array)-1])
print(array[0] + array[-1])
print(array[int((len(array)+1)/2)])

for i in array:
    print(i, end=" ")

print()

for i in range(int(len(array)/2)):
    print(array[i], end=" ")
