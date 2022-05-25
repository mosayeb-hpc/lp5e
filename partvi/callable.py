# File callable.py
from __future__ import print_function


def square(arg):
    return arg ** 2


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)


if __name__ == "__main__":
    sobject = Sum(2)
    pobject = Product(3)
    actions = [square, sobject, pobject.method, Negate]

    for act in actions:
        print(act(5), end=', ')
    print()

    m = map(lambda act: act(5), actions)
    print(list(m))

    print(actions[-1](5))

    table = {act(5): act for act in actions}
    for (key, value) in table.items():
        print('%2s => %s' % (key, value))
