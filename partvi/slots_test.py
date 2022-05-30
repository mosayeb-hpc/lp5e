# File slots-test.py
from __future__ import print_function
import timeit

base = """
Is = []
for i in range(1000):
    I = C()
    I.a, I.b, I.c, I.d = 1, 2, 3, 4
    t = I.a + I.b + I.c + I.d
Is.append(t)
"""

stmt = """
class C:
    __slots__ = ['a', 'b', 'c', 'd']
""" + base

print('slots   =>', end=' ')
print(min(timeit.repeat(stmt=stmt, number=1000, repeat=3)))

stmt = """
class C:
    pass
""" + base

print('Nonslots=>', end=' ')
print(min(timeit.repeat(stmt=stmt, number=1000, repeat=3)))
