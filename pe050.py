#!/usr/bin/env python3
'''
Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
'''

from itertools import count

from prime import primes

if __name__ == '__main__':
    best_length = 21
    best_prime = 953
    for start_idx in count():
        if sum(primes[start_idx:start_idx + best_length + 1]) > 1000000:
            # The smallest sum of primes for this start point is over one
            # million, so we're not going to find any new results.
            break
        for end_idx in count(start_idx + best_length + 1):
            sum_of_primes = sum(primes[start_idx:end_idx])
            if sum_of_primes > 1000000:
                # Over one million, so try the next start index.
                break
            if sum_of_primes in primes:
                # Better than anything we've seen before.  We know it has to
                # have a longer sequence since the shortest sequence length
                # we'd loop over is longer than the previous best result.
                best_prime = sum_of_primes
                best_length = end_idx - start_idx
    print(best_prime)
