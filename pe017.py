#!/usr/bin/env python3
'''
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
'''


def words(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif n == 30:
        return 'thirty'
    elif n == 40:
        return 'forty'
    elif n == 50:
        return 'fifty'
    elif n == 60:
        return 'sixty'
    elif n == 70:
        return 'seventy'
    elif n == 80:
        return 'eighty'
    elif n == 90:
        return 'ninety'
    elif n <= 99:
        units = n % 10
        tens = n - units
        return words(tens) + words(units)
    elif n <= 999 and n % 100 == 0:
        hundreds_digit = n // 100
        return words(hundreds_digit) + 'hundred'
    elif n <= 999:
        tens_units = n % 100
        hundreds = n - tens_units
        return words(hundreds) + 'and' + words(tens_units)
    elif n == 1000:
        return 'onethousand'
    else:
        raise RuntimeError('Unexpected number {}'.format(n))

if __name__ == '__main__':
    count = 0
    for i in range(1, 1001):
        count += len(words(i))
    print(count)
