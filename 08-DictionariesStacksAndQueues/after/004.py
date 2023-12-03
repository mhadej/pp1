hotels_in_krakow = [
    { "name":"Sky",          "price": 320.00 },
    { "name":"Metropol",     "price": 480.00 },
    { "name":"New Port",     "price": 420.00 },
    { "name":"Aparthotel",   "price": 390.00 }
]

hotels_in_sopot = [
    { "name":"Focus",        "price" : 510.00 },
    { "name":"Aqua",         "price" : 345.00 },
    { "name":"La Boutique",  "price" : 390.00 },
    { "name":"Marina",       "price" : 410.00 }
]

def hotel_list(hotels):
    hotellist  = []    
    for i in hotels:
        for key, value in i.items():
            if key == "name":
                hotellist.append(value)
    return hotellist

def avg_price(hotels):
    hotelprice = []
    for i in hotels:
        for key, value in i.items():
            if key == "price":
                hotelprice.append(value)
    return hotelprice

print(f"Hotels in Krakow: {", ".join(hotel_list(hotels_in_krakow))}")
print(f"Average price of hotels in Krakow: {int((sum(avg_price(hotels_in_krakow))/len(hotels_in_krakow)))}")

print(f"\nHotels in Sopot: {", ".join(hotel_list(hotels_in_sopot))}")
print(f"Average price of hotels in Sopot: {int((sum(avg_price(hotels_in_sopot))/len(hotels_in_sopot)))}")