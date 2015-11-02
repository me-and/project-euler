#!/usr/bin/env python3
'''
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from sys import argv
from itertools import takewhile

from prime import prime_generator

if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 2000000
    print(sum(takewhile(lambda x: x < target, prime_generator())))
