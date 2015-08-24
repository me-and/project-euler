#!/usr/bin/env python3
'''
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

from collections import defaultdict
from sys import argv

from pe003 import prime_generator


# Very similar to (and should probably be combined with) pe003.prime_factors.
#
# Alternatively, fix the inefficiency where we work through the factors one at
# a time, meaning the prime generator gets run every time rather than only
# once.
def power_prime_factor(n):
    factors = defaultdict(int)
    primes = prime_generator()
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
        if p ** 2 > n:
            if n != 1:  # Happens if the original n was prime.
                factors[n] += 1
            return factors


if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 20

    powers = defaultdict(int)

    for n in range(2, target + 1):
        prime_powers = power_prime_factor(n)
        for k in prime_powers:
            powers[k] = max(powers[k], prime_powers[k])

    total = 1
    for k in powers:
        total *= k ** powers[k]
    print(total)
