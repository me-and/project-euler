#!/usr/bin/env python3
'''
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from sys import argv

from prime import prime_factors

if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 600851475143
    print(max(prime_factors(target)))
