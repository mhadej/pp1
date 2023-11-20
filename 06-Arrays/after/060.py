# matrix

def identity_matrix(n):
    array = [[0 for i in range(n)] for i in range(n)]
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if i == j:
                array[i][j] = 1

    return array

for i in identity_matrix(3):
    print(i)

for i in identity_matrix(5):
    print(i)

for i in identity_matrix(8):
    print(i)
