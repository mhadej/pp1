ean = input("Enter EAN-13 article number: ")

if(len(ean) == 13):
    print("Article nuber is correct")
    if ean[0:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Article number incorrect")