from scripts.primes import is_prime

primes = [2]
n = 3

while len(primes) < 10001:
    if is_prime(n, primes):
        primes.append(n)

    n += 2

print(primes[-1])