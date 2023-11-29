import json

with open(r"08-DictionariesStacksAndQueues\during\json.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")