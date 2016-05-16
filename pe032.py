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

GOAL_SET = frozenset('123456789')

if __name__ == '__main__':
    # Multiply things and see if the result is pandigital.  Only need to go up
    # to four-digit numbers because if either of the products is a five-digit
    # number the result will have at least five digits, and the total number of
    # digits must be nine.
    products = set()
    for multiplicand in range(1, 10000):
        for multiplier in range(1, 10000 // multiplicand):
            product = multiplier * multiplicand
            if set(str(multiplicand) +
                   str(multiplier) +
                   str(product)) == GOAL_SET:
                products.add(product)

    print(sum(products))
