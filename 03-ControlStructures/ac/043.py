a = 4
b = 15

print(f"{"*"*b}")
a -= 1

while a:
    if a > 1:
        print(f"*{" "*(b-2)}*")
        a -= 1
    elif a > 0:
        print(f"{"*"*b}")
        a -= 1