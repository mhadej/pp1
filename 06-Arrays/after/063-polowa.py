array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 0]]

def transpose_matrix(array):
    copy = []

    for i in range(0, len(array[0])): # 0, 1, 2, 3, 4
        table = []
        for j in range(0, len(array)): # 0, 1
            table.append(array[j][i])
        copy.append(table)

    print(copy)

transpose_matrix(array1)
transpose_matrix(array2)