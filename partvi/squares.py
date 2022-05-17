# File: squares.py

class Squares:
    def __init__(self, start, stop) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            sq = self.start ** 2
            self.start += 1
            return sq
        else:
            raise StopIteration


class Squares1:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __len__(self):
        return self.stop - self.start

    def __getitem__(self, index):
        index += self.start
        if index < self.stop:
            sq = index ** 2
            index += 1
            return sq
        else:
            raise StopIteration


if __name__ == "__main__":
    for i in Squares(0, 10):
        print(i, end=' ')
    print("")
    Z = zip(range(0, 10), Squares(0, 10))
    print(list(Z))
    X = Squares1(0, 10)
    for v in X:
        print(v)
    print(list(X))