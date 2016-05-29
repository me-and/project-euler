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

from prime import is_prime, prime_generator


class SquareGenerator(object):
    def __init__(self):
        self.squares = set()
        self.max_square = 0
        self._generator = self._square_generator()

    def _square_generator(self):
        for i in count(1):
            self.max_square = i ** 2
            self.squares.add(self.max_square)
            yield self.max_square

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)

    def is_square(self, num):
        if num > self.max_square:
            for sq in self:
                if num == sq:  # Generated num as a square
                    return True
                elif num < sq:  # Passed num without generating it
                    return False
        else:
            return num in self.squares


is_square = SquareGenerator().is_square


def meets_goldbach(num):
    for prime in prime_generator():
        if prime > num:
            # We've cycled through all the primes less than num, so there can
            # be no prime that meets the conjecture.
            return False
        if is_square((num - prime) // 2):
            return True


if __name__ == '__main__':
    for num in count(3, 2):
        if is_prime(num):  # Not composite, so skip.
            continue
        if not meets_goldbach(num):
            print(num)
            break
