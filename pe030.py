#!/usr/bin/env python3
'''
Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
'''

from sys import argv

# Experimentation shows there is a six-digit number that has this property, but
# no such seven digit numbers.

if __name__ == '__main__':
    try:
        power = int(argv[1])
        num_digits = int(argv[2])
    except IndexError:
        power = 5
        num_digits = 6

    powers = {str(n): n ** power for n in range(10)}

    running_total = 0
    for number in range(10, 10 ** num_digits):
        power_sum = sum(powers[n] for n in str(number))
        if number == power_sum:
            running_total += number
            print(number)

    print('Total:', running_total)
