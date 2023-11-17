def counter(string, letter):
    nr = 0
    for i in string:
        if i.upper() == letter.upper():
            nr += 1
    return nr