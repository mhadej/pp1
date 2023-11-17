def f(number):
    number = str(number)
    sum = 0
    counter = 1
    łopata = [True]*9

    for i in number:
        if number.find(i, counter) > 0:
            sum += int(i)
            if i == "1" and łopata[0]:
                sum += int(i)
                łopata[0] = False
            elif i == "2" and łopata[1]:
                sum += int(i)
                łopata[1] = False   
            elif i == "3" and łopata[2]:
                sum += int(i)
                łopata[2] = False   
            elif i == "4" and łopata[3]:
                sum += int(i)
                łopata[3] = False   
            elif i == "5" and łopata[4]:
                sum += int(i)
                łopata[4] = False   
            elif i == "6" and łopata[5]:
                sum += int(i)
                łopata[5] = False   
            elif i == "7" and łopata[6]:
                sum += int(i)
                łopata[6] = False   
            elif i == "8" and łopata[7]:
                sum += int(i)
                łopata[7] = False   
            elif i == "9" and łopata[8]:
                sum += int(i)
                łopata[8] = False 
        counter += 1

    return sum

print(f(1027))
print(f(230335))
print(f(513553007))
