def masking(credit_card):
    number = list(credit_card)
    for i in range (10):
        number[(i+2)] = "*"
    number = ''.join(number)
    return number