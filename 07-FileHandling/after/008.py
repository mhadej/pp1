#losowe w osobnej linii

import random

try:
    with open(r"07-FileHandling\after\random.txt", r"w") as file:
        for i in range(1, 51):
            number = random.randint(100, 999)
            if i == 50:
                file.write(str(number))
            else:
                file.write(str(number) + "\n")
except FileNotFoundError as err:
    print(err)