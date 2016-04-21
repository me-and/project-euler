#!/usr/bin/env python3
'''
Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.

    *131*  673   234   103    18
    *201*  *96* *342*  965   150
     630   803  *746* *422*  111
     537   699   497  *121*  956
     805   732   524   *37* *331*

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80
matrix, from the top left to the bottom right by only moving right and down.
'''

from itertools import product
import os.path
from sys import argv


if __name__ == '__main__':
    try:
        path = argv[1]
    except IndexError:
        path = os.path.join('pe081', 'matrix.txt')
    matrix = []
    with open(path) as matrix_file:
        for line in matrix_file:
            matrix.append(list(map(int, line.strip().split(','))))

    for x, y in product(range(len(matrix[0])), range(len(matrix))):
        # Just replace the values in the matrix with the score to get to that
        # point in the matrix as we calculate them; we're going to be reliably
        # working from top left to bottom right, so that's safe.
        if x == y == 0:
            # The score at this point is just the score for this cell anyway.
            pass
        elif x == 0:
            matrix[y][x] += matrix[y - 1][x]
        elif y == 0:
            matrix[y][x] += matrix[y][x - 1]
        else:
            matrix[y][x] += min(matrix[y][x - 1], matrix[y - 1][x])

    print(matrix[-1][-1])
