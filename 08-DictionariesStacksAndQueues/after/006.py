import json

try:
    with open(r"08-DictionariesStacksAndQueues\after\MOCK_DATA.json") as file:
        jsonfile = json.load(file)
        array = []
        directory = {}
        with open(r"08-DictionariesStacksAndQueues\after\limited.json", r"w") as file2:
            for i in jsonfile:
                for key, value in i.items():
                    if key == "name" or key == "surname" or key == "student_id":
                        directory.update({key:value})
                array.append(directory.copy())
                
            json.dump(array, file2, indent=5)
except FileNotFoundError as err:
    print(err)