def f(dice):
    table = list(dice)
    sum = 0
    buffer = 0
    max = 0

    for i in range(len(table)-1):
        if table[i] == table[i+1]:
            sum += 1
            if sum > buffer:
                buffer = sum
                max = table[i]
        else:
            sum = 0
    return max

print(f("5233165554211"))
print(f("23133"))
print(f('111144444111'))