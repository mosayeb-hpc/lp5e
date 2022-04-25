"Test the relative speed of iteration tool alternatives."


import sys
import timer2 as timer
from math import sqrt
reps = 10000
repslist = list(range(reps))


def power_mat():
    for i in repslist:
        res = sqrt(i)
    return res


def power_exp():
    for i in repslist:
        res = i ** .5
    return res


def power_pow():
    for i in repslist:
        res = pow(i, .5)
    return res


print(sys.version)
for func in (power_mat, power_exp, power_pow):
    (bestof, result) = timer.bestoftotal(func, _reps1=5, _reps=1000)
    print('%-9s: %.5f => %s' % (func.__name__, bestof, result))
