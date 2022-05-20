# File: __iadd__.py

from __future__ import print_function
from ast import Num


class Number:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return '<' + self.__class__.__name__ + ' %s>' % self.val

    def __add__(self, other):
        print('add', self, other)
        if isinstance(other, Number):
            other = other.val
        return Number(self.val + other)

    def __iadd__(self, other):
        print('iadd', self, other)
        if isinstance(other, Number):
            other = other.val
        self.val += other
        return self

    __radd__ = __add__


if __name__ == "__main__":
    x = Number(0)
    y = Number(0)
    z = Number(0)
    x += 1
    y += 2
    z += 3
    print(x)
    x += y
    print(x)
    z = 1 + x + y + 2
    print(z)
