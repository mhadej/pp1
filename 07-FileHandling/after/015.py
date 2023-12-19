#policz średnią piotrka szeligi

import re

pattern = r"\d\.\d"

try:
    with open(r"after\grades.txt") as file:
        grades = re.findall(pattern, file.read())
        sum = 0

        for grade in grades:
            sum += float(grade)

        print(f"Arithmetic mean of Peter's grades: {round(sum/len(grades), 2)}")
except FileNotFoundError as err:
    print(err)