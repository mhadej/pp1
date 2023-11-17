decimal = int(input("Enter decimal number: "))
buffer = decimal
rest = 0
result = ""

while decimal:
    rest = decimal%2
    if rest:
        decimal = decimal/2 - 0.5
        result = "1" + result
    else:
        decimal /= 2
        result = "0" + result

print(f"{buffer}(10) = {result}(2)")