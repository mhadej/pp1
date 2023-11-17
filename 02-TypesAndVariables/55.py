x = input("Enter four-digit binary number: ")

result = 0

if x[0] == "1":
    result += 8
if x[1] == "1":
    result += 4
if x[2] == "1":
    result += 2
if x[3] == "1":
    result += 1

print("Binary number in decimal: ", result)