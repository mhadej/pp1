#1-50 w osobnej linii

try:
    with open(r"07-FileHandling\after\onefifty.txt", r"w") as file:
        for i in range(1, 51):
            if i == 50:
                file.write(str(i))
            else:
                file.write(str(i) + "\n")
except FileNotFoundError as err:
    print(err)