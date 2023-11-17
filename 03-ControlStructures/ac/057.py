n = int(input("Enter N: "))

prime   = []
complex = []

i = 2

while len(prime) < n:
    if i in complex:
        cepibula = 0
    else:
        prime.append(i)
        for x in range (2, n*n):
            complex.append(i*x)
    i += 1

print(prime)