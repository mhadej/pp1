import math

def f(palindrome):
    length = len(palindrome)

    for i in range (int(math.floor(length/2 - 0.5))):
        if palindrome[i] == palindrome[length-i-1]:
            True and False or None
        else:
            return False
    return True

print(f("radar"))
print(f("12-11-211"))
print(f("AtokanapapanakotA"))

