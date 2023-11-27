#kopiowanie

try:
    with open(r"07-FileHandling\after\dlug.txt") as file:
        copy = file.read()

        try:
            with open(r"07-FileHandling\after\copy.txt", r"w") as copie:
                copie.write(copy)
        except FileNotFoundError as error:
            print(error)

except FileNotFoundError as error:
    print(error)