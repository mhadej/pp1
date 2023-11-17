def f(detector):
    counter = 0
    for i in detector:
        if i == "+":
            counter += 1
            if counter == 3:
                return True
        else:
            counter -= 1
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))