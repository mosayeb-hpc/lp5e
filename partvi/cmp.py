# File: cmp.py (only python 2)

from __future__ import print_function


class Cmp:
    def __init__(self, data):
        self.data = data

    def __cmp__(self, other):
        return cmp(self.data, other)


class C:
    def __init__(self, data):
        self.data = data

    def __cmp__(self, other):
        return ((self.data > other) - (self.data < other))


if __name__ == "__main__":
    x1 = Cmp(3)
    x2 = C(5)
    for x in [x1, x2]:
        print('-' * 40)
        print('x = %s' % x.data)
        print('x > 4 %s' % (x > 4))
        print('x < 4 %s' % (x < 4))
        print('x == 4 %s' % (x == 4))
        print('x != 4 %s' % (x != 4))
