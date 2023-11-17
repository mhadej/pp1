def f(amount_to_pay):
    counter = 0
    while amount_to_pay:
        if amount_to_pay >= 5:
            amount_to_pay -= 5
            counter += 1
        elif amount_to_pay >= 2:
            amount_to_pay -= 2
            counter += 1
        elif amount_to_pay == 1:
            amount_to_pay -= 1
            counter += 1
    return counter

print(f(23))
print(f(8))
print(f(2))
print(f(0))