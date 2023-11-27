#csv

import csv

try:
    with open(r"07-FileHandling\after\studentslist.txt") as file:
        reader = csv.reader(file)

        for line in reader:
            age = line.index('age')
            break
        
        for line in reader:
            if int(line[age]) < 30:
                print(f'{line[0]} {line[1]} {line[4]}')
            
except FileNotFoundError as err:
    print(err)