def numbers(n):
    string = ""
    for i in range(n):
        string += str(i+1) + " "
    return string

print(numbers(15))
print(numbers(7))