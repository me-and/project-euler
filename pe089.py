#!/usr/bin/env python3
'''
Roman numerals

For a number written in Roman numerals to be considered valid there are basic
rules which must be followed.  Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number of
numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see [About... Roman Numerals][0]
for the definitive rules for this problem.

[0]: https://projecteuler.net/about=roman_numerals

Find the number of characters saved by writing each of these in their minimal
form.

Note: you can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
'''

import os.path

ROMAN_SUBTRACTIVE_PAIRS = {'IV': 4,
                           'IX': 9,
                           'XL': 40,
                           'XC': 90,
                           'CD': 400,
                           'CM': 900}

ROMAN_DIGITS = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}

INTEGER_CONVERSIONS = ((1000, 'M'),
                       (900, 'CM'),
                       (500, 'D'),
                       (400, 'CD'),
                       (100, 'C'),
                       (90, 'XC'),
                       (50, 'L'),
                       (40, 'XL'),
                       (10, 'X'),
                       (9, 'IX'),
                       (5, 'V'),
                       (4, 'IV'),
                       (1, 'I'))


FILE_PATH = os.path.join('pe089', 'roman.txt')


def roman_to_integer(string):
    '''Convert a Roman numeral string to an integer.

    Correct for valid Roman numerals, but does not check numerals are valid and
    may produce unintuitive results if given invalid Roman numerals (e.g. 'IL'
    is parsed as 51, not 49; the standard valid way to write 49 is XLIX).
    '''
    integer = 0
    while string:
        if string[:2] in ROMAN_SUBTRACTIVE_PAIRS:
            integer += ROMAN_SUBTRACTIVE_PAIRS[string[:2]]
            string = string[2:]
        else:
            integer += ROMAN_DIGITS[string[0]]
            string = string[1:]
    return integer


def integer_to_roman(integer):
    '''Convert an integer to a minimal Roman numeral.'''
    string = ''
    for test_int, roman in INTEGER_CONVERSIONS:
        while integer >= test_int:
            string += roman
            integer -= test_int
    return string


def idealize(roman):
    return integer_to_roman(roman_to_integer(roman))


if __name__ == '__main__':
    difference = 0
    with open(FILE_PATH) as roman_file:
        for line in roman_file:
            roman = line.strip()
            difference += len(roman) - len(idealize(roman))
    print(difference)
