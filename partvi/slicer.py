# File: slicer.py (python 2)
from __future__ import print_function


class Slicer:
    def __init__(self, seq):
        it = iter(seq)
        self.data = list(it)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __getslice__(self, i, j):
        seq = list()
        ln = len(self.data)

        if i < -ln:
            i = 0
        elif i < 0:
            i += ln
        if j < -ln:
            j = 0
        elif j < 0:
            j += ln

        while i < j and i < len(self.data):
            seq.append(self.data[i])
            i += 1
        return Slicer(seq)

    def __repr__(self):
        return '%s' % self.data[::]


class C:
    def __index__(self):
        return 255


if __name__ == "__main__":
    X = Slicer(range(10))
    print(X[1:])
    print(X[-1::-1])
    Y = C()
    L = list(range(300))
    print(bin(Y))
    print(L[Y:])
