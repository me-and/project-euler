#!/usr/bin/env python3
'''
Champernowne's constant

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...
                 ^

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''

from itertools import count
from sys import argv


def gen_digits():
    for i in count(1):
        for c in str(i):
            yield c


if __name__ == '__main__':
    if len(argv) > 1:
        indices = set(map(int, argv[1:]))
    else:
        indices = {1, 10, 100, 1000, 10000, 100000, 1000000}

    product = 1
    for i, d in enumerate(gen_digits(), start=1):
        if i in indices:
            product *= int(d)
            indices.remove(i)
            if not indices:  # Have all the results we need
                break

    print(product)
