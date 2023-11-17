import letters

string = input("Enter a sentence: ")
letter = input("Enter a letter: ")

print(f"The number of letter {letter}: {letters.counter(string, letter)}")