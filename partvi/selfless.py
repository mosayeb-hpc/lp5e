# File selfless (python 3.X)
from __future__ import print_function


class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2


if __name__ == "__main__":
    X = Selfless(2)
    print(X.normal(3, 4))
    print(Selfless.normal(X, 3, 4))
    print(Selfless.selfless(3, 4))
    print(type(X.normal))
    print(type(X.selfless))
    print(type(Selfless.normal))
    print(type(Selfless.selfless))
