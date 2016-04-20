#!/usr/bin/env python3
'''
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def chain_length(n, chain_lengths):
    if n not in chain_lengths:
        chain_lengths[n] = chain_length(next_collatz(n), chain_lengths) + 1
    return chain_lengths[n]


def print_collatz_chain(n):
    while n != 1:
        print(n, end=' -> ')
        n = next_collatz(n)
    print(n)


if __name__ == '__main__':
    chain_lengths = {1: 1}
    max_starter = 1
    max_length = 1
    for i in range(1, 1000000):
        length = chain_length(i, chain_lengths)
        if length > max_length:
            max_starter = i
            max_length = length
    print(max_starter)
    print_collatz_chain(max_starter)
