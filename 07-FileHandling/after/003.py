#pięć linii, stop

try:
    with open(r"07-FileHandling\after\dlug.txt") as file:
        while(True):
            for i in range(5):
                print(file.readline(), end="")
            enter = input()

            if enter != "":
                break
            
except FileNotFoundError as error:
    print(error)