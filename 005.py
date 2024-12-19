from math import prod

divisors = range(1, 21)
factors = []

for n in divisors:
    while n > 1:
        for factor in factors:
            if not n % factor:
                n /= factor

        break

    if n != 1:
        factors.append(int(n))

print(prod(factors))