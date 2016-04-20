#!/usr/bin/env python3
'''
Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

         *3*
       *7*  4
      2  *4*  6
    8   5  *9*  3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o) '''

import os.path

from pe018 import Node


def parse_rows():
    node_rows = []
    with open(os.path.join('pe067', 'triangle.txt')) as triangle:
        for i, line in enumerate(triangle):
            node_row = []
            line = line.strip()
            for j, num in enumerate(line.split()):
                if i == 0:
                    lparent = None
                    rparent = None
                elif j == 0:
                    lparent = None
                    rparent = node_rows[i - 1][j]
                elif j == i:
                    lparent = node_rows[i - 1][j - 1]
                    rparent = None
                else:
                    lparent = node_rows[i - 1][j - 1]
                    rparent = node_rows[i - 1][j]
                node = Node(int(num), lparent, rparent)
                if lparent is not None:
                    lparent.rchild = node
                if rparent is not None:
                    rparent.lchild = node
                node_row.append(node)
            node_rows.append(node_row)
    return node_rows[0][0]

if __name__ == '__main__':
    root_node = parse_rows()
    print(root_node.max_score())
