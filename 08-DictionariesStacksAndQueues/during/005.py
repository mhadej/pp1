import json

movie = {
    "title":"Pirates of the Caribbean: At World's End",
    "director": "Gore Verbinski",
    "actors": ["Johnny Depp", "Orlando Bloom"],
    "producer": "Walt Disney",
    "year": 2007
}

try:
    with open(r"08-DictionariesStacksAndQueues\during\favorite.json", r"w") as file:
        json.dump(movie, file, indent=3)

except FileNotFoundError as err:
    print(err)