import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values
for n in range(0,361):
    x += [n]

# create y values
for n in x:
    y += [math.sin(math.radians(n))]

# display chart

plt.plot(x, y)
plt.show()