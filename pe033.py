#!/usr/bin/env python3
'''
Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

from fractions import Fraction


def is_curious(num, den):
    # Assume we've already discarded the trivial examples.
    str_num = str(num)
    str_den = str(den)
    common_digits = set(str_num) & set(str_den)
    for digit in common_digits:
        new_num = int(str_num.replace(digit, '', 1))
        new_den = int(str_den.replace(digit, '', 1))
        if Fraction(num, den) == Fraction(new_num, new_den):
            return True
    return False

if __name__ == '__main__':
    running_product = Fraction(1)
    for den in range(10, 100):
        if den % 10 == 0:
            continue
        for num in range(10, den):
            if is_curious(num, den):
                running_product *= Fraction(num, den)

    print(running_product.denominator)
