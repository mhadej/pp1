import random

score = random.randint(1,6)

print("Dice rolled: ", score)
print("Special number: ", score == 1 or score == 6 )