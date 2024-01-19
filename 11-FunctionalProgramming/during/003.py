distance = int(input("Enter distance: "))
hours    = int(input("Enter hours: "))
minutes  = int(input("Enter minutes: "))

def avg_speed(distance, hours, minutes):
    return round(distance/(hours+(minutes/60)), 1)

print(f"Average speed: {avg_speed(distance, hours, minutes)} km/h")

average_speed = lambda d, h, m: round(d/(h+(m/60)), 1)

print(f"Average speed: {average_speed(distance, hours, minutes)} km/h")
