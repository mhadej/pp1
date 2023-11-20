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

first = []
last  = []

for i in range(len(array)):
    first.append(array[i][0])
    last.append(array[i][-1])

for i in range(len(array)):
    array[i][0]  = last[i]
    array[i][-1] = first[i]


for i in array:
    print(i)  