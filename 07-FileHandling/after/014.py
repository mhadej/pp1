#liczenie słów >5 liter

import re

pattern = r"[^ .,?!]{6,}"

try:
    with open(r"07-FileHandling\after\dlug.txt") as file:
        for line in file:
            words = re.findall(pattern, line)

            for word in words:
                print(word)

except FileNotFoundError as err:
    print(err)