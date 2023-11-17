x = int(input("Wprowadz x "))
y = int(input("Wprowadz y "))
z = int(input("Wprowadz z "))

l = x+y+z
p= l/2

area = (p*(p-x)*(p-y)*(p-z))**(1/2)

print("Circumference: ",l, " area: ",area)