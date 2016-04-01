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

from prime import prime_factors_seed


if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 20

    powers = defaultdict(int)

    # Keep track of prime_generator instances, starting with None, to allow
    # pre-seeding of the next prime generator.
    prime_generator = None

    for n in range(2, target + 1):
        prime_powers, prime_generator = prime_factors_seed(n, prime_generator,
                                                           preserve_seed=False)
        for k in prime_powers:
            powers[k] = max(powers[k], prime_powers[k])

    total = 1
    for k in powers:
        total *= k ** powers[k]
    print(total)
