array = [
    [1,  2,  3 ],
    [4,  5,  6 ],
    [7,  8,  9 ],
    [10, 11, 12],
    [13, 14, 15],
]

for i in array:
    print(i)
print()

first = array[0].copy()
last  = array[-1].copy()

for i in range(len(first)):
    array[-1][i] = first[i]
    array[0][i] = last[i]

for i in array:
    print(i)

    