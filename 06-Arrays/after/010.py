array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
index = 0
max = 0
counter = 0

for i in array:
    if len(i) > max:
        index = counter
        max = len(i)
    counter += 1

print(f"Longest name: {array[index]}")