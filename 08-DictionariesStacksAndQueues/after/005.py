radiotelephony_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

def alphabet_to_nato(name):
    for i in name.upper():
        for key, value in radiotelephony_alphabet.items():
            if key == i:
                print(value)

alphabet_to_nato("Hubert")
alphabet_to_nato("uek")

try:
    with open(r"08-DictionariesStacksAndQueues\after\ICAO.txt", r"w") as file:
        for key, value in radiotelephony_alphabet.items():
            file.write(f"{key} {value}\n")
except FileNotFoundError as err:
        print(err)