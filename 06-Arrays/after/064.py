def onedimension(array):
    temp_array = array

    lista = []

    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            lista.append(array[i][j])

    print(lista)

onedimension([[2, 3], [1, 5]])
onedimension([[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]])
onedimension([[2, 1], [3, 5], [7, 4], [2, 6]])