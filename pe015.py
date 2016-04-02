#!/usr/bin/env python3
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

     ___      _        _
        |      |_       |      |___     |_       |
        |        |      |_         |      |_     |___

How many such routes are there through a 20×20 grid?
'''

# Consider an n x m grid.  If the first move is right, the routes available are
# those on a (n-1) x m grid; if the first move is down, the routes available
# are those on an n x (m-1) grid.  Huzzah, induction!
#
# For the base case, it's pretty easy to show that a 1xn grid has n+1 routes
# through it.
#
# So f(x, y) = f(x-1, y) + f(x, y-1), and f(1, n) = f(n, 1) = n+1
#
# I could try working out the formula that satisfies that, but frankly it's
# easy enough to code from here.

from sys import argv

stored_routes = {}


def routes(x, y):
    if y == 1:
        return x + 1
    if x == 1:
        return y + 1
    if (x, y) in stored_routes:
        return stored_routes[(x, y)]
    num_routes = routes(x-1, y) + routes(x, y-1)
    stored_routes[(x, y)] = num_routes
    return num_routes


if __name__ == '__main__':
    try:
        sides = int(argv[1])
    except IndexError:
        sides = 20

    print(routes(sides, sides))
