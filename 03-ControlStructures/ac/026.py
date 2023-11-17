x = 2
y = -2

if x and y:
    if x > 0:
        if y > 0:
            print(f"Point ({x}, {y}) is located in the first quadrant.")
        else:
            print(f"Point ({x}, {y}) is located in the fourth quadrant.")
    else:
        if y > 0:
            print(f"Point ({x}, {y}) is located in the second quadrant.")
        else:
            print(f"Point ({x}, {y}) is located in the third quadrant.")
else:
    print("Point P is located in the midde (0,0)")