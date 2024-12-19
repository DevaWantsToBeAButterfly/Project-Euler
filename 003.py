from scripts.primes import primes_in_range

dividend = 600851475143
primes = primes_in_range(dividend)
prime_factors = []

while dividend > 1:
    for n in primes:
        if not dividend % n:
            dividend /= n
            prime_factors.append(n)

print(max(prime_factors))