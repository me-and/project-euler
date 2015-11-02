#!/usr/bin/env python3
'''
Sum square difference

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''
from sys import argv

# Expanding the terms shows:
#
#     (1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)
#         = ((1^2 + 2^2 + ... + n^2)
#             + 2×((1×2 + 1×3 + ... + 1×n)
#                 + (2×3 + 2×4 + ... + 2×n)
#                 + ... + ((n-1)×n))
#           - (1^2 + 2^2 + ... + n^2)
#         = 2 × ((1×2 + 1×3 + ... + 1×n)
#             + (2×3 + 2×4 + ... + 2×n)
#             + ... + ((n-1) × n)
#         = 2 × 1 × (2 + 3 + ... + n) +
#           2 × 2 × (3 + 4 + ... + n) +
#           ... +
#           2 × (n-2) × ((n-1) + n) +
#           2 × (n-1) × n
#
# Feels like there should be some obvious solution here, but frankly I think
# the quickest solution is just brute force...

if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 100

    # Triangle numbers.  I can remember this formula at least!  Use // to get
    # integer division; we know it'll be an integer anyway and it means we
    # don't need to worry about floats confusing anything.
    square_sum = (target * (target + 1) // 2) ** 2

    sum_square = sum((x ** 2 for x in range(target + 1)))

    print(square_sum - sum_square)
