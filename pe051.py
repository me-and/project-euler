#!/usr/bin/env python3
'''
Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
'''

from itertools import compress, groupby, product

from prime import primes


def all_equal(iterable):
    # From https://docs.python.org/3/library/itertools.html#itertools-recipes
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def replace_digits(string, replacements, digit):
    return ''.join(digit if r else c for c, r in zip(string, replacements))


def test_prime(prime):
    prime_string = str(prime)

    # Iterate over tuples of possible characters we could replace; 56**3, for
    # example, would be a prime of 56003 with a replacements tuple of (False,
    # False, True, True, False).
    for replacements in product((True, False), repeat=len(prime_string)):
        # Skip if we're replacing all or none of the digits, since that's not
        # interesting, and also skip if not all the digits being replaced are
        # equal, since in that case the prime we're looking at isn't one of the
        # primes we'll generate.
        if (all_equal(replacements) or
                not all_equal(compress(prime_string, replacements))):
            continue

        # Allow replacement with 0 only if the first digit isn't one that's
        # being replaced.
        if replacements[0]:
            replacement_digits = '123456789'
        else:
            replacement_digits = '0123456789'

        if sum(int(replace_digits(prime_string, replacements, digit)) in primes
               for digit in replacement_digits) >= 8:
            return True

    # Tried all the possible ways to replaced digits without finding a
    # solution.
    return False

if __name__ == '__main__':
    for prime in primes.range(56004, None):
        if test_prime(prime):
            print(prime)
            break
