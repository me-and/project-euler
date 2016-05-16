#!/usr/bin/env python3
'''
Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

from itertools import permutations

if __name__ == '__main__':
    # We're looking for x, y and z such that x * y == z and all the digits 1-9
    # occur exactly once.  Consider permutations of the digits 1-9, consider
    # all the splits of such digits, then check whether each split satisfies
    # x * y == z.
    products = set()
    for permutation in permutations('123456789'):
        for lslice in range(1, 8):
            for rslice in range(lslice + 1, 9):
                multiplier = int(''.join(permutation[:lslice]))
                multiplicand = int(''.join(permutation[lslice:rslice]))
                product = int(''.join(permutation[rslice:]))

                if multiplier * multiplicand == product:
                    products.add(product)

    print(sum(products))
