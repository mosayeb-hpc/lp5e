# File: adder.py

from __future__ import print_function


class Adder:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        self.value += other


class AddRepr(Adder):
    def __repr__(self):
        return 'AddRepr(%s)' % self.value


class AddStr(Adder):
    def __str__(self):
        return '[Value: %s]' % self.value


class AddBoth(AddRepr, AddStr):
    def __repr__(self):
        return 'AddBoth(%s)' % self.value


if __name__ == "__main__":
    x = AddRepr(2)
    x + 1
    a, b = str(x), repr(x)
    print(a, b)

    x = AddStr(22)
    x + 11
    a, b = str(x), repr(x)
    print(a, b)

    x = AddBoth(222)
    x + 111
    a, b = str(x), repr(x)
    print(a, b)
