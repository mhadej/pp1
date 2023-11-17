import math

def f(expression):
    sum = int(expression[0])

    for i in range (0, len(expression)-1, 2):
        if expression[i+1] == "+":
            sum += int(expression[i+2])
        else:
            sum -= int(expression[i+2])
    return sum

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))