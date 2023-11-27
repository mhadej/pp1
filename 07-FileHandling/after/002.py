#liczenie linii

name = input("Enter file name: ")

try:
    with open(f"07-FileHandling/after/{name}.txt") as myfile:
        counter = 0

        for line in myfile:
            counter += 1
    print(f"File name: {name}.txt\nNumber of lines: {counter}")

except FileNotFoundError as error:
    print(error)