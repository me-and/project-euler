#!/usr/bin/env python3
'''
Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2  =   0.5
    1/3  =   0.(3)
    1/4  =   0.25
    1/5  =   0.2
    1/6  =   0.1(6)
    1/7  =   0.(142857)
    1/8  =   0.125
    1/9  =   0.(1)
    1/10 =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
'''

from sys import argv


# Repeatedly perform long division -- multiplying by 10 and dividing by n --
# until we get either 0 (in which case there's no cycle) or a remainder that
# we've seen before, in which case use the dict mapping remainders we've seen
# to their decimal position, compared to the current position, to get the cycle
# length.
def cycle_length(n):
    remainders = {}
    numerator = 1
    position = 0

    while numerator != 0 and numerator not in remainders:
        remainders[numerator] = position
        numerator = (numerator * 10) % n
        position += 1

    if numerator == 0:
        return 0
    else:
        return position - remainders[numerator]


if __name__ == '__main__':
    try:
        max_denom = int(argv[1])
    except IndexError:
        max_denom = 999

    print(max(((n, cycle_length(n)) for n in range(1, max_denom + 1)),
              key=lambda x: x[1])[0])
