def f(text):
    if len(text) > 1:
        letters = list(text)
        new_text = text[0]
        for i in range(len(letters)-1):
            new_text += "-" + letters[i+1] 
        return new_text
    else:
        return text
    
print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))