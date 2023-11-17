def occurs(number, array):
    return number in array

array = [2, 1, 3, 7]    
print(occurs(2, array))
print(occurs(1, array))
print(occurs(4, array))

x = int(input("Check if number is in array: "))

print(occurs(x, [15, 38, 7, 23, 14]))