#kopiowanie linia po linii

try:
    with open(r"07-FileHandling\after\dlug.txt") as file:
        try:
            with open(r"07-FileHandling\after\copylines.txt", r"w") as copie:
                for line in file:
                    copie.write(line)
        except FileNotFoundError as error:
            print(error)

except FileNotFoundError as error:
    print(error)