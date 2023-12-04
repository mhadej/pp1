import json

print(f'{"Date":<16}{"Buying Rate":<16}{"Selling Rate":<16}')
print("="*44)

try:
    with open(r"08-DictionariesStacksAndQueues\after\euro.json") as file:
        json_file = json.load(file)
        
        for key, value in json_file.items():
            if key == "rates":
                for i in value:
                    for key1, value1 in i.items():
                        if key1 != "no":
                            print(f'{value1:<16}', end="")
                    print()

except FileNotFoundError as err:
    print(err)