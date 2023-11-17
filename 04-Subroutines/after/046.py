def f(password):
    strong_pass = {}

    for i in password:
        if i in strong_pass:
            strong_pass[i] += 1
        else:
            strong_pass[i] = 1
    
    if len(strong_pass.keys()) >= 6:
        return True
    else:
        return False

print(f("ax15"))
print(f("book12"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))
