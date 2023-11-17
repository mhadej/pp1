def f(number, even):
    number = str(number)
    sum = 0
    if even:
        for i in number:
            if not int(i)%2:
                sum += int(i)
    else:
        for i in number:
            if int(i)%2:
                sum += int(i)
    return sum

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))