dogs_age = int(input("Enter dog's age in human years: "))
first_two = 2
human_years = 0

for x in range(dogs_age):
    if first_two:
        human_years += 10.5
        first_two-=1
    else:
        human_years +=4
    x-=1

print(f"The dog's age in dog's years is {human_years} years")