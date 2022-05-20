# File: commuter.py

from __future__ import print_function


class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self, other)
        return self.val + other

    def __repr__(self):
        return '<' + self.__class__.__name__ + ': %s>' % self.val


class Commuter1(Commuter):
    def __radd__(self, other):
        print('radd', other, self)
        return other + self.val


class Commuter2(Commuter):
    def __radd__(self, other):
        return self.__add__(other)


class Commuter3(Commuter):
    def __radd__(self, other):
        return self + other


class Commuter4(Commuter):
    def __add__(self, other):
        print('add', self, other)
        return self.val + other

    __radd__ = __add__


class Commuter5(Commuter):
    def __add__(self, other):
        print('add', self, other)
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)

    def __radd__(self, other):
        print('radd', other, self)
        return Commuter5(self.val + other)


class Commuter6(Commuter):
    def __add__(self, other):
        print('add', self, other)
        if isinstance(other, Commuter6):
            other = other.val
        return Commuter6(self.val + other)

    __radd__ = __add__


if __name__ == "__main__":
    def func(x, y, z):
        print(x + 1)
        print(1 + y)
        print(x + y)
        print(x + y + z)

    for Klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5, Commuter6):
        print('-' * 60)
        x = Klass(88)
        y = Klass(99)
        z = Klass(100)
        func(x, y, z)
