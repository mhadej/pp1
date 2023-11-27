#with zamiast open()

with open(r"07-FileHandling\after\filename.txt") as myfile:
    print(myfile.read(), end="")