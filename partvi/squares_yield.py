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
