countries = [
    {"name":"Poland",   "population": 38},
    {"name":"Germany",  "population": 60},
    {"name":"France",   "population": 50},
    {"name":"Czechia",  "population": 15},
    {"name":"Slovakia", "population": 20}
]

print("COUNTRY    POPULATION (in mln)")

i = 0

while(len(countries) > i):
    print(f'{countries[i]["name"]:10} {countries[i]["population"]:<10}')
    i += 1