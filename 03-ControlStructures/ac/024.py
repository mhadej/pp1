hour = input("Enter time (24-hour format): ")

if hour[1] == ':':
    print(f"Time in 12-hour format: {hour}am")
else:
    hourint = int(hour[0:2])
    if hourint == 12:
        print(f"Time in 12-hour format: {hourint}:{hour[3:6]}pm")
    elif hourint >= 12:
        print(f"Time in 12-hour format: {hourint-12}:{hour[3:6]}pm")
    else:
        print(f"Time in 12-hour format: {hourint}:{hour[3:6]}am")