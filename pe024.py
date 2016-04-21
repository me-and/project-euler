#!/usr/bin/env python3
'''
Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
'''

from sys import argv
from itertools import islice, permutations

if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 1000000

    # Use islice to discard the first `target - 1` permutations.
    print(''.join(next(islice(permutations('0123456789', 10),
                              target - 1,
                              None))))
