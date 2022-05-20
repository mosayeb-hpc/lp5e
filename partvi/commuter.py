# File: commuter.py

from __future__ import print_function


class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


if __name__ == "__main__":
    x = Commuter1(88)
    y = Commuter1(99)
    z = Commuter1(100)

    print('x + 1 = %s' % (x + 1))
    print('1 + y = %s' % (1 + y))
    print('x + y = %s' % (x + y))
    print()
    print('x + y + z = %s' % (x + y + z))
    print()
    print('x + (y + z) = %s' % (x + (y + z)))
