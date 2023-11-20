array = [[-38, 19], [5, 40], [-7,11], [29,16]]

min = 0
max = 0
indexmin = [0, 0]
indexmax = [0, 0]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] > max:
            max = array[i][j]
            indexmax = [i, j]
        if array[i][j] < min:
            min = array[i][j]
            indexmin = [i, j]
    
print(f"The smallest value of {array[indexmin[0]][indexmin[1]]} is located in [{indexmin[0]}, {indexmin[1]}].")
print(f"The largest value of {array[indexmax[0]][indexmax[1]]} is located in [{indexmax[0]}, {indexmax[1]}].")