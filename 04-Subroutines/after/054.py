def f(product_code):
    digits = list(product_code)
    sum = int(digits[0]) + int(digits[1]) + int(digits[2])
    if str(sum%7) == digits[3]:
        return True
    else:
        return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))