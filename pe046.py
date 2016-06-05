#!/usr/bin/env python3
'''
Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
'''

from itertools import count

from prime import primes
from sequence import MonatonicIncreasingSequence


squares = MonatonicIncreasingSequence(i ** 2 for i in count(1))


def meets_goldbach(num):
    for prime in primes:
        if prime > num:
            # We've cycled through all the primes less than num, so there can
            # be no prime that meets the conjecture.
            return False
        if (num - prime) // 2 in squares:
            return True


if __name__ == '__main__':
    for num in count(3, 2):
        if num in primes:  # Not composite, so skip.
            continue
        if not meets_goldbach(num):
            print(num)
            break
