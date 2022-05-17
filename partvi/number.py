# File: number.py

from cmath import pi


class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __del__(self):
        # Destructor: Object reclamation of Number
        print('%s: %s deleted' % (self.__class__.__name__, self.data))


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        S = ""
        for x in self.data:
            S = S + str(x) + ' '
        return S


class C:
    def __index__(self):
        return 255


class StepperIndex:
    def __getitem__(self, index):
        return self.data[index]


if __name__ == "__main__":
    n = Number(100)
    n = n - 200
    print(n.data)
    X = C()
    print(hex(X), oct(X), bin(X), end='\t')
    print('\n')
    L = list(range(300))
    print(L[X:])
    Z = StepperIndex()
    Z.data = 'Spam'
    print(Z[1])
    for item in Z:
        print(item, end=' ')
    print("")
