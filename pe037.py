#!/usr/bin/env python3
'''
Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from prime import primes


def truncatable_prime(prime):
    string = str(prime)
    for i in range(1, len(string)):
        if int(string[i:]) not in primes:
            return False
        if int(string[:-i]) not in primes:
            return False
    return True

if __name__ == '__main__':
    truncatable_primes = []
    for prime in primes.range(10, None):
        if truncatable_prime(prime):
            truncatable_primes.append(prime)
            if len(truncatable_primes) >= 11:
                break

    print(sum(truncatable_primes))
