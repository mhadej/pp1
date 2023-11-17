car_speed = float(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140 

if speed_limit_min <= car_speed < speed_limit_max:
    print("Good :)")
else:
    print("Warning: invalid car speed!")