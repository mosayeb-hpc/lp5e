# File: skipper.py (python 3 and 2)

from __future__ import print_function
from more_itertools import random_combination

from pkg_resources import yield_lines


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        ln = len(self.wrapped)
        for i in range(0, ln, 2):
            yield self.wrapped[i]


if __name__ == "__main__":
    alpha = "abcdef"
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
    print("")
    print('a' in skipper)
