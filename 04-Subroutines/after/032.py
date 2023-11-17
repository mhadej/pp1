def f(n):
    table = [0, 1]

    for i in range(n):
        table.append(table [i+1] + table[i])
    return table[n-1]

print(f(5))
print(f(9))