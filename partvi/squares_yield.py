# File: squares_yield.py

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop):
            yield value ** 2


if __name__ == "__main__":
    for i in Squares(1, 6):
        print(i, end=' ')
    print("")
    S = Squares(1, 6)
    I = iter(S)
    print(next(I), next(I))
    J = iter(S)
    print(next(J))
    S = Squares(1, 4)
    for i in S:
        for j in S:
            print('%s:%s' % (i,j), end=' ')
    print("")
