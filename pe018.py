#!/usr/bin/env python3
'''
Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

         *3*
       *7*  4
      2  *4*  6
    8   5  *9*  3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                75
                              95  64
                            17  47  82
                          18  35  87  10
                        20  04  82  47  65
                      19  01  23  75  03  34
                    88  02  77  73  07  63  67
                  99  65  04  28  06  16  70  92
                41  41  26  56  83  40  80  70  33
              41  48  72  33  47  32  37  16  94  29
            53  71  44  65  25  43  91  52  97  51  14
          70  11  33  28  77  73  17  78  39  68  17  57
        91  71  52  38  17  14  91  43  58  50  27  29  48
      63  66  04  68  89  53  67  30  73  16  69  87  40  31
    04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
'''

ROWS = ((75,),
        (95, 64),
        (17, 47, 82),
        (18, 35, 87, 10),
        (20, 4, 82, 47, 65),
        (19, 1, 23, 75, 3, 34),
        (88, 2, 77, 73, 7, 63, 67),
        (99, 65, 4, 28, 6, 16, 70, 92),
        (41, 41, 26, 56, 83, 40, 80, 70, 33),
        (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
        (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
        (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
        (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
        (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
        (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23))


class Node(object):
    def __init__(self, score, lparent, rparent):
        self.score = score
        self.topscore = None
        self.lparent = lparent
        self.rparent = rparent
        self.lchild = None
        self.rchild = None

    def __repr__(self):
        return '<{} object {}>'.format(self.__class__.__name__, self.score)

    def max_score(self):
        if self.topscore is None:
            if self.lchild is None and self.rchild is None:
                self.topscore = self.score
            else:
                self.topscore = self.score + max(self.rchild.max_score(),
                                                 self.lchild.max_score())
        return self.topscore


def parse_rows():
    node_rows = []
    for i in range(len(ROWS)):
        node_row = []
        for j in range(len(ROWS[i])):
            if i == 0:
                lparent = None
                rparent = None
            elif j == 0:
                lparent = None
                rparent = node_rows[i - 1][j]
            elif j == len(ROWS[i]) - 1:
                lparent = node_rows[i - 1][j - 1]
                rparent = None
            else:
                lparent = node_rows[i - 1][j - 1]
                rparent = node_rows[i - 1][j]
            node = Node(ROWS[i][j], lparent, rparent)
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
