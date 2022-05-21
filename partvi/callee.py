# File: callee.py

from __future__ import print_function


class Callee:
    def __call__(self, *pargs, **kargs):
        print("Called:", pargs, kargs)

class Power:
    def __init__(self, val):
        self.base =val

    def __call__(self, exp):
        return self.base ** exp


if __name__ == "__main__":
    x = Callee()
    x(1, 2, 3, a=1)
    x(*range(10), **dict(a='a', b='b', c={'1': '1', '2': '2'}))
    print()
    y = Power(2)
    for i in range(65):
        print("%2s =>%+20s" % (i, y(i)))
