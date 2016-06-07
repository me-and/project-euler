#!/usr/bin/env python3
'''
Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from sys import argv

def is_right_triangle(a, b, c):
    # Assumes a < c and b < c.
    return (a ** 2) + (b ** 2) == (c ** 2)


if __name__ == '__main__':
    try:
        maximum = int(argv[1])
    except IndexError:
        maximum = 1000

    solutions = {}
    for p in range(1, maximum + 1):
        # Find integer solutions for a + b + c == p and a ≤ b ≤ c.  Thus
        # a ≤ p/3, and b ≤ (p - a)/2
        for a in range(1, p // 3):
            for b in range(1, (p - a) // 2):
                c = p - a - b
                if is_right_triangle(a, b, c):
                    solutions.setdefault(p, []).append((a, b, c))

    print(max(solutions.keys(), key=lambda x: len(solutions[x])))
