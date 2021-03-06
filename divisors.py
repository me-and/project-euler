'''
Functions for working with divisors
'''

from math import sqrt


def divisors(x):
    '''Generate the proper divisors of a number

    The generated divisors are not in order.
    '''
    # Based broadly on http://stackoverflow.com/a/171779/220155
    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0:
            yield i
            if i != 1 and i * i != x:
                yield x // i


def ordered_divisors(x):
    '''Generate the proper divisors of a number, in order.'''
    # Based broadly on http://stackoverflow.com/a/171779/220155
    not_yet_yielded = []
    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0:
            yield i
            if i != 1 and i * i != x:
                not_yet_yielded.insert(0, x // i)
    for i in not_yet_yielded:
        yield i
