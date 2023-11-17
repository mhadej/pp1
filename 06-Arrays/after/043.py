text = "An apple a day keeps the doctor away"

def words(text):
    return len(text.split())

def order(text):
    table = text.split()
    buffer = 0
    shuffle = 1

    while(shuffle):
        shuffle = 0
        for i in range(len(table)-1):
            if len(table[i+1]) > len(table [i]):
                buffer = table[i]

                table[i] = table[i+1]
                table[i+1] = buffer

                shuffle += 1

    return table

def alphabet(text):
    text = text.lower().split()
    text = sorted(text)
    return text

print(alphabet(text))