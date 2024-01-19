test_results = [ {"name":"Peter",   "result": 27},
                 {"name":"Anna",    "result": 63},
                 {"name":"Robert",  "result": 92},
                 {"name":"Paul",    "result": 46},
                 {"name":"Barbara", "result": 52}]

for person in test_results:
    for key, value in person.items():
        if key == "result" and 50 < value < 70:
                print(person["name"])