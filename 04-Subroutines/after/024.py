def f(n):
    string = "*"
    n -= 1

    for i in range(n):
        string += "/*"

    return string

print(f(4))
print(f(1))
print(f(10))