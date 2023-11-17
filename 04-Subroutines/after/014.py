def f(binary_number):
    x = 0
    for i in binary_number:
        if i == "0" or i == "1":
            x = x
        else:
            x += 1
    if x:
        return False
    else:
        return True
    
x = input("Enter a binary number: ")
print(f"Is number {x} valid? {f(x)}")