#!/usr/bin/env python3
'''
Double-base palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''

from sys import argv


def bin_palindrome(n):
    string = bin(n)[2:]
    return string == string[::-1]


def dec_palindrome(n):
    string = str(n)
    return string == string[::-1]


if __name__ == '__main__':
    try:
        maximum = int(argv[1])
    except IndexError:
        maximum = 1000000

    print(sum(x for x in range(1, maximum + 1)
              if bin_palindrome(x) and dec_palindrome(x)))
