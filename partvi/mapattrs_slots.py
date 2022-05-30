# mapattrs-slots.py: test __slots__ attribute inheritance
from mapattrs import mapattrs, trace


class A(object):
    __slots__ = ['a', 'b']
    x = 1
    y = 2


class B(A):
    __slots__ = ['b', 'c']


class C(A):
    x = 2


class D(B, C):
    z = 3

    def __init__(self):
        self.name = 'bob'


if __name__ == "__main__":
    I = D()
    trace(mapattrs(I, bysource=True))
    print('-' * 80)
    trace(mapattrs(I))
