def f(n):
    if n == 1:
        return 2

    prime = []
    non_prime = []

    while True:
        for i in range(2, n*n):
            if i not in non_prime:
                prime.append(i)
                if len(prime) == n:
                    return prime[n-1]
                for j in range(2, 10):
                    non_prime.append(i*j)

print(f(1))
print(f(5))
print(f(10))
