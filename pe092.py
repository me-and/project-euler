#!/usr/bin/env python3
'''
Square digit chains

A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

    44 -> 32 -> 13 -> 10 -> 1 -> 1
    85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop.  What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

_arrives_at_89 = {89: True, 1: False}


def arrives_at_89(num):
    if num not in _arrives_at_89:
        _arrives_at_89[num] = arrives_at_89(sum(int(x) ** 2 for x in str(num)))
    return _arrives_at_89[num]

if __name__ == '__main__':
    print(sum(1 for num in range(1, 10000001) if arrives_at_89(num)))
