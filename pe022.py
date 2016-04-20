#!/usr/bin/env python3
'''
Names scores

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import os.path


LETTER_SCORES = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))


def score_name(name):
    return sum(LETTER_SCORES[l] for l in name)


if __name__ == '__main__':
    with open(os.path.join('pe022', 'names.txt')) as namefile:
        names_string = namefile.read()
    names = names_string.split(',')
    names = [name.strip('"') for name in names]
    names = sorted(names)
    total = 0
    for i, name in enumerate(names, 1):
        total += i * score_name(name)
    print(total)
