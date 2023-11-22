file = open(r'during/shopping.txt', 'a', encoding="UTF-8")

read_product = True
counter = 0

while read_product:
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(f'{counter}. {product}\n')
    else:
        read_product = False

file.close()