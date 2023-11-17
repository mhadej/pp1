for i in range(6, -1, -3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()

i2 = 6
j2 = 1

while i2 >= 0:
    while j2 < 4:
        print(f" {i2 + j2}", end="")
        j2 += 1
    i2 -= 3
    j2 = 1
    print()