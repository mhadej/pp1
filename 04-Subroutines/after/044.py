def f(name):
    name = name.strip()
    string = name[0]
    lenght = len(name)

    for i in range(lenght):
        if name[i] == " ":
            string += name[i+1]
    return string

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))