def hotel_list(hotels):
    i=0
    hotels1 = []
    while i < len(hotels):
        hotels_data = hotels[i]
        hotels1.append(hotels_data["name"])
        i += 1
    return hotels1
        
def avg_price(hotels):
    i=0
    avg_price = 0
    while i < len(hotels):
        hotels_data = hotels[i]
        avg_price = hotels_data["price"] + avg_price
        i += 1
    return round(avg_price,0)    

hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

print(f"\n\nHotels in Krakow: ", end = "")

for i in hotel_list(hotels_in_Krakow):
    print (f"{i}",end ="")

print(f"\nAverage hotel price in Krakow: {avg_price(hotels_in_Krakow)}")

print(f"Hotels in Sopot: ", end = "")
for i in hotel_list(hotels_in_Sopot):
    print (f"{i}", end = "")
print(f",\nAverage hotel price in Sopot: {avg_price(hotels_in_Sopot)}")

if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
    cheper_hotels = "Kraków"
else:
    cheper_hotels = "Sopot"

print(f"Cheaper hotels in: {cheper_hotels}")