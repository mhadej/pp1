def f(nr1, nr2, nr3):
    highest = nr1
    if nr2 > highest:
        highest = nr2
    if nr3 > highest:
        highest = nr3
    
    lowest = nr1
    if nr2 < lowest:
        lowest = nr2
    if nr3 < lowest:
        lowest = nr3
    
    return highest - lowest

print(f(7,4,9))
print(f(2,12,8))
