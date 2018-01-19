#!/usr/bin/env python3
'''
Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

from itertools import count, permutations

if __name__ == '__main__':
    largest_pandigital = 0
    largest_integer = None
    largest_n = None

    for pandigital in permutations('123456789'):
        string = ''.join(pandigital)

        # Note the integer being multiplied must be a substring of the
        # pandigital string on the left-hand side, since the first
        # multiplication is ×1.  The integer must have at least one digit and
        # at most four (since n must be greater than two, and a four-digit
        # number multiplied by both one and two must each have at least four
        # digits, and we need a total of nine digits.)
        for int_digits in range(1, 5):
            new_pandigital = string[:int_digits]
            integer = int(new_pandigital)
            for i in count(2):
                new_pandigital += str(integer * i)
                if len(new_pandigital) >= 9:
                    # Have got up to an n that is sufficiently large.
                    break
            if string == new_pandigital:
                pandigital = int(string)
                if pandigital > largest_pandigital:
                    largest_pandigital = pandigital
                    largest_integer = integer
                    largest_n = i

    print(largest_pandigital)
