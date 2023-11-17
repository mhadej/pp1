def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)-1):
            if array1[i] != array2[i]:
                return False
        return True
    else:
        return False
    
print(compare(["water", "book", "sky"], ["water", "book", "sky"]))
print(compare([True, False], [True, False, True]))
print(compare([5,3,1],[5,3,1]))
print(compare([3,2,1],[3,2]))