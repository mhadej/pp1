pin = "0805"
correct = 3

while correct:
    enter = input("Enter the PIN code: ")
    if enter == pin:
        print("Access granted!")
        raise SystemExit
    else:
        correct -= 1
        print("Incorrect...")

print("Sorry, your payment card has been blocked")