import math

height = 180
feet = math.floor(height/30.48)
inches = round(height/2.54) - feet * 12

print(height,"cm is ",feet, "feet and ", inches, " inches")