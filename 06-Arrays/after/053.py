array =  [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = j+1
        array[j][i] = j+1
    break

for i in range(1, len(array)):
    for j in range(1, len(array[i])):
        array[i][j] = array[i][0] * array[0][j]

for i in array:
    for j in i:
        print(j, end= " ")
    print()