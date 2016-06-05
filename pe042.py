#!/usr/bin/env python3
'''
Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so
the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, how many are triangle words?
'''

from itertools import count
import os.path

from sequence import MonatonicIncreasingSequence

LETTER_SCORES = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))


triangles = MonatonicIncreasingSequence((i * (i + 1)) // 2 for i in count(1))


def score_word(word):
    word = word.strip('"')
    return sum(LETTER_SCORES[letter] for letter in word)


def triangle_word(word):
    return score_word(word) in triangles

if __name__ == '__main__':
    with open(os.path.join('pe042', 'words.txt')) as word_file:
        word_list = word_file.read().strip().split(',')
    print(sum(map(triangle_word, word_list)))
