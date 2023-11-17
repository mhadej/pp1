i1 = 0
i2 = 1

print("0 1 ", end="")
for x in range(1,9):
    i3 = i1 + i2
    print(f"{i3} ", end="")
    i1 = i2
    i2 = i3