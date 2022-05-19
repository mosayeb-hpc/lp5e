# File: squares_manual.py

from __future__ import print_function


class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def gen(self):
        for value in range(self.start, self.stop):
            yield value ** 2


if __name__ == "__main__":
    for i in Squares(1, 6).gen():
        print(i, end=' ')
    print("")
