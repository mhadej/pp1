i = 1

while i <= 30:
    if not i%3 and not i%5:
        print("BINGO")
    elif not i%3:
        print("THREE")
    elif not i%5:
        print("FIVE")
    else:
        print(f"{i}")
    i += 1
