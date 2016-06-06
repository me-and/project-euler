#!/usr/bin/env python3
'''
Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
'''

from itertools import count

from prime import prime_factors

if __name__ == '__main__':
    sequence = 0
    for number in count(1):
        if len(prime_factors(number)) == 4:
            sequence += 1
            if sequence == 4:
                print(number - 3)
                break
        else:
            sequence = 0
