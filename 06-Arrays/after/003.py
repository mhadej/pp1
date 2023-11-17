array = [[True,False],[True,True],[False,False,False]]

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = not array[i][j]

for i in array:
    print(i)