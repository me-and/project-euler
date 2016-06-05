#!/usr/bin/env python3
'''
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
'''

from sys import argv
from itertools import islice

from prime import primes

if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 10001

    # Use islice to discard the first `target - 1` primes.
    print(next(islice(primes, target - 1, None)))
