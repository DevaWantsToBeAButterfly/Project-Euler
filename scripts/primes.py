from math import sqrt, floor

def is_prime(number):
    for n in range(2, floor(sqrt(number)) + 1):
        if not number % n:
            return False

    return True

def primes_in_range(upper_limit):
    primes = []
    for n in range(2, floor(sqrt(upper_limit)) + 1):
        if is_prime(n):
            primes.append(n)

    return primes