# File: skipper.py (python 3 and 2)

from __future__ import print_function


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.data = wrapped
        self.offset = 0

    def __next__(self):
        ln = len(self.data)
        if self.offset < ln:
            item = self.data[self.offset]
            self.offset += 2
            return item
        else:
            raise StopIteration

    next = __next__


if __name__ == "__main__":
    alpha = "abcdef"
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
    print("")
