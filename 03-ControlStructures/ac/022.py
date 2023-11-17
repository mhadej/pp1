washing_product = "jacket"
rinse = False
spin = True

total_time = 0

if washing_product == "shoes":
    total_time += 20
elif washing_product == "jacket":
    total_time += 40
else:
    total_time += 70

if rinse: total_time += 15
if spin : total_time += 9

print(f"Total washing time: {total_time}min")