def different(a1, a2, a3):
    if a1 == a2 == a3:
        return False
    else:
        return True

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))

print(f"Are numbers {a1}, {a2}, {a3} different? {different(a1, a2, a3)}")

