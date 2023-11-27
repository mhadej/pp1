#łączenie ryb z warzywami

try:
    with open(r"07-FileHandling\after\grainsandbread.txt") as list1, open(r"07-FileHandling\after\meatandfish.txt") as list2:
        try:
            with open(r"07-FileHandling\after\allproducts.txt", r"w") as list:
                list.write(list1.read())
                list.write("\n")
                list.write(list2.read())
        except FileNotFoundError as error:
            print(error)

except FileNotFoundError as error:
    print(error)