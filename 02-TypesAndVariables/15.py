register = input("Enter vehicle registration number: ")

print("Is this car from Cracow?")

if(register[0:2].upper()=="KR"):
    print("True")
else:
    print("False")
