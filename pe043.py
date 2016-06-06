#!/usr/bin/env python3
'''
Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

    d_2 d_3 d_4 = 406 is divisible by 2
    d_3 d_4 d_5 = 063 is divisible by 3
    d_4 d_5 d_6 = 635 is divisible by 5
    d_5 d_6 d_7 = 357 is divisible by 7
    d_6 d_7 d_8 = 572 is divisible by 11
    d_7 d_8 d_9 = 728 is divisible by 13
    d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from itertools import product

ALL_DIGITS = frozenset('0123456789')


if __name__ == '__main__':
    # Iterate over the numbers d_2 d_3 d_4, d_5 d_6 d_7 and d_8 d_9 d_10, check
    # whether the number is pandigital, then whether the other substrings
    # divide suitably.
    #
    # We don't actually care about d_1 until the very last minute; if we have
    # d_2 through d_10 we can assert the number is pandigital for some value of
    # d_1 we compute later, and we have all the digits we need to check for
    # divisibility already.
    #
    # For looping through the multiples, just use `range` to loop, starting at
    # the lowest multiple greater than 100 of the relevant number and
    # continuing to 1000.
    running_sum = 0
    for triple in product(range(100, 1000, 2),
                          range(105, 1000, 7),
                          range(102, 1000, 17)):
        string = ''.join(map(str, triple))
        string_set = set(string)
        if len(string_set) != 9:  # Not pandigital
            continue
        if (int(string[1:4]) % 3 != 0 or
                int(string[2:5]) % 5 != 0 or
                int(string[4:7]) % 11 != 0 or
                int(string[5:8]) % 13 != 0):
            # Not all divisible correctly.
            continue
        remaining_digit = next(iter(ALL_DIGITS - string_set))
        running_sum += int(remaining_digit + string)
    print(running_sum)
