name = input("Enter your name: ")

for x in name:
    result = f"{x}({ord(x)})"
    print(f"{result}" ,end=' ')