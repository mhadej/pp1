import mymath
import mykeyboard

while True:
    x = mykeyboard.read_number()
    y = mymath.generate_number()

    print(f"Computer number: {y}")

    if x == y:
        print("YOU WON!")
        break
    else:
        print("Try again!")