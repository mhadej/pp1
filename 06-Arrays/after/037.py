array1 = [2, 1, 3, 7]
array2 = [2, 1, 7, 3]
array3 = [1, 2, 5, 5]

maks = 0

for i in array2:
    if i not in array1:
        print("Array is not a subset of the second one")
        break
    else:
        maks += 1
    if maks/len(array2) == 1:
        print("Array is a subset of the second one")
    
maks = 0

for i in array3:
    if i not in array1:
        print("Array is not a subset of the second one")
        break
    else:
        maks += 1
    if maks/len(array3) == 1:
        print("Array is a subset of the second one")
    