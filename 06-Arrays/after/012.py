array = [12, 6, 4, 9, 10]

def star(n):
    x = str(n) + " " + "*"*n

    return x

for i in array:
    print(star(i))