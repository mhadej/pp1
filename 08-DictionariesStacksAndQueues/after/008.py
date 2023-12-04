import json
import csv

try:
    with open(r"08-DictionariesStacksAndQueues\after\products.csv") as file:
        csv_file = csv.reader(file)
        ultimate = []
        kys = []
        for row in csv_file:
            for i in row:
                kys.append(i)
            break
        for row in csv_file:
            directory = {}

            for j in kys: #[Product, Quantity, Price]
                for i in range(len(row)): #[milk, 8, 4.25]
                    directory.update({kys[i]:row[i]})
            ultimate.append(directory.copy())
        try:
            with open(r"08-DictionariesStacksAndQueues\after\products.json", r"w") as file:
                json.dump(ultimate, file, indent=4)

        except FileNotFoundError as err2:
            print(err2)

except FileExistsError as err:
    print(err)