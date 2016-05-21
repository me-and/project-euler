#!/usr/bin/env python3
'''
Circular primes

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
'''

from prime import is_prime, prime_generator
from sys import argv


def rotations(n):
    '''Rotations of n, excluding n itself.'''
    string = str(n)
    return (int(string[i:] + string[:i]) for i in range(1, len(string)))


def circular_prime(n):
    '''Assuming n is prime, is it a circular prime?'''
    for i in rotations(n):
        if not is_prime(i):
            return False
    return True


if __name__ == '__main__':
    try:
        maximum = int(argv[1])
    except IndexError:
        maximum = 1000000

    circular_primes = set()
    for p in prime_generator():
        if p > maximum:
            break
        if circular_prime(p):
            circular_primes.add(p)

    print(len(circular_primes))
