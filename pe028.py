#!/usr/bin/env python3
'''
Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    *21* 22  23  24 *25*
     20  *7*  8  *9* 10
     19   6  *1*  2  11
     18  *5*  4  *3* 12
    *17* 16  15  14 *13*

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
'''

from itertools import islice
from sys import argv


def generate_corners():
    jump = 2
    point = 1
    yield point

    while True:
        for corner in range(4):
            point += jump
            yield point
        jump += 2


if __name__ == '__main__':
    try:
        size = int(argv[1])
    except IndexError:
        size = 1001

    # Number of cells on the diagonals, counting the centre once, for an n x n
    # square with odd n is 2n - 1.  This can be trivially shown by induction.
    print(sum(islice(generate_corners(), 2 * size - 1)))
