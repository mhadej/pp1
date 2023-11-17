array = [-15, 8, -31, 47, -2, 19]

min  = array[0]
maxi = array[0]

for i in array:
    if i > maxi:
        maxi = i
    if i < min:
        min = i

print(maxi, min)