#potęgi 1-10

try:
    with open(r"07-FileHandling\after\power.txt", r"w") as file:
        for i in range(1, 11):
            file.write(f"{i}, {i**2}, {i**3} \n")

except FileNotFoundError as err:
    print(err)