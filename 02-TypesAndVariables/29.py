import random

x = random.randint(1,6)
answer = int(input("Guess the score "))

print("Is your guess the same as rolled dice? ", x == answer, f"({x})")