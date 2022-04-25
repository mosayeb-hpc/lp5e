from functools import reduce
from math import factorial
from timeit import repeat


def factcd(N):
    if N == 1:
        return 1
    else:
        return N * factcd(N - 1)


def factrd(N):
    return reduce(lambda x, y: x * y, range(1, N + 1))


def factlp(N):
    p = 1
    for i in range(1, N + 1):
        p *= i
    return p


def factmt(N):
    return factorial(N)


def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1])


def rev2(S):
    return ''.join(reversed(S))


def rev3(S):
    return S[::-1]


print(factcd(6), factrd(6), factlp(6), factmt(6))
print(factcd(500) == factrd(500) == factlp(500) == factmt(500))

for func in (factcd, factrd, factlp, factmt):
    print(func.__name__, min(repeat(stmt=lambda: func(500), number=1000, repeat=5)))

S = 'SPAM'
S1 = S * 100
print(rev1(S), rev2(S), rev3(S))

for rev in (rev1, rev2, rev3):
    print(rev.__name__, min(repeat(stmt=lambda: rev(S1), number=1000, repeat=3)))
