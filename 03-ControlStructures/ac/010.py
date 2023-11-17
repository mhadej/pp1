curr_price = 170.00
prev_price = 200.00

discount = (prev_price-curr_price)/prev_price 

print(f"Current product price: {curr_price}")
print(f"Previous product price: {prev_price}")

if discount >= 0.1:
    print(f"Buy the product!\nPrice reduced by {discount*100}%")
else:
    print(f"The discount ({discount*100}%) is too low.")