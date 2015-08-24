#!/usr/bin/env python3
'''
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from itertools import combinations_with_replacement


def is_palendrome(n):
    string = str(n)
    return string == string[::-1]


def products():
    seen = set()
    for x, y in combinations_with_replacement(range(100, 1000), 2):
        product = x * y
        if product not in seen:
            yield product
            seen.add(product)


if __name__ == '__main__':
    print(max((n for n in products() if is_palendrome(n))))
