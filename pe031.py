#!/usr/bin/env python3
'''
Coin sums

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

from sys import argv

COINS = (200, 100, 50, 20, 10, 5, 2, 1)


# The use of memo as an argument here is a bit of an ugly hack to give a static
# variable -- because the value of memo is initialized when the function is
# defined and never again, each call to the function gets the same dict, i.e.
# the one that will have been modified by previous calls to the function.
def num_ways(goal, max_coin=200, memo={}):
    # If we've reached the goal, or there're only 1p coins left to use, we're
    # done.
    if goal == 0 or max_coin == 1:
        return 1

    # Maximum coin we can use is the smallest of the coins that fits in the
    # goal and the largest coin we've previously used.
    for coin in COINS:
        if goal >= coin and max_coin >= coin:
            max_coin = coin
            break

    # Check if we already know the answer
    if (goal, max_coin) in memo:
        return memo[(goal, max_coin)]

    ways = 0
    for coin in COINS:
        if max_coin >= coin:
            ways += num_ways(goal - coin, coin)

    memo[(goal, max_coin)] = ways
    return ways

if __name__ == '__main__':
    try:
        goal = int(argv[1])
    except IndexError:
        goal = 200

    print(num_ways(goal))
