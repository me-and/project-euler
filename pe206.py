#!/usr/bin/env python3
'''
Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
'''

# Consider the last digit of our target integer: it must be 0, since that is the
# only way for the square to have a last digit of 0.  Further, if we square a
# number ending in "0", we know the result must end in "00".  Thus we simplify
# the problem to only needing an integer whose square has the form
# 1_2_3_4_5_6_7_8_900, and we know this integer must be a multiple of 10.

from math import sqrt

if __name__ == '__main__':
    lower_bound = int(sqrt(1020304050607080900))
    upper_bound = int(sqrt(1929394959697989900))

    for test_val in range(lower_bound, upper_bound, 10):
        if str(test_val ** 2)[::2] == '1234567890':
            print(test_val)
            break
