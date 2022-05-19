# File: contains.py

from __future__ import print_function


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print("get[%s]:" % index, end='')
        return self.data[index]

    def __iter__(self):
        print("iter=> ", end='')
        self.ix = 0
        return self

    def __next__(self):
        print("next:", end='')
        if self.ix < len(self.data):
            item = self.data[self.ix]
            self.ix += 1
            return item
        else:
            raise StopIteration

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data
    next = __next__


if __name__ == "__main__":
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end=' | ')

    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
    print()
