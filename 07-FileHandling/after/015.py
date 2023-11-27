#policz średnią piotrka szeligi

import re

pattern = r"\d\.\d"

try:
    with open(r"07-FileHandling\after\grades.txt") as file:
        grades = re.findall(pattern, file.read())
        counter = 0
        sum = 0

        for grade in grades:
            counter += 1
            sum += float(grade)

        print(f"Arithmetic mean of Peter's grades: {round(sum/counter, 2)}")
except FileNotFoundError as err:
    print(err)