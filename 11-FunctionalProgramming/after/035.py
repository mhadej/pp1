results = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

counter = 0 

for result in results:
    if not ( result * 0.98 <= 500 <= result * 1.02 ):
        counter += 1

print(f'Incorrectly filled: {int(counter/len(results)*100)}%')