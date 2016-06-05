#!/usr/bin/env python3
'''
Quadratic primes

Euler discovered the remarkable quadratic formula:

    n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

from itertools import count, product
from sys import argv

from prime import primes


def quad(a, b, n):
    return (n ** 2) + (a * n) + b

if __name__ == '__main__':
    if len(argv) == 1:  # No arguments
        min_a = min_b = -1000
        max_a = max_b = 1000
    elif len(argv) == 2:  # Single argument
        arg = int(argv[1])
        min_a = min_b = -arg
        max_a = max_b = arg
    elif len(argv) == 3:  # Two arguments
        args = (int(argv[1]), int(argv[2]))
        min_a = -args[0]
        max_a = args[0]
        min_b = -args[1]
        max_b = args[1]
    elif len(argv) == 5:  # Four arguments
        min_a = int(argv[1])
        max_a = int(argv[2])
        min_b = int(argv[3])
        max_b = int(argv[4])
    else:
        raise RuntimeError("Unrecognized arguments: {!r}".format(argv[1:]))

    most_primes_found = 0
    for a, b in product(range(min_a, max_a + 1), range(min_b, max_b + 1)):
        primes_found = 0
        for n in count():
            if quad(a, b, n) in primes:
                primes_found += 1
            else:
                if primes_found > most_primes_found:
                    most_primes_found = primes_found
                    best_a = a
                    best_b = b
                break
    print(best_a * best_b)
