"Test the relative speed of iteration tool alternatives."


import sys
import timer2 as timer
reps = 10000
repslist = list(range(reps))


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))


def genExpres():
    return list(abs(x) for x in repslist)


def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)
for func in (forLoop, listComp, mapCall, genExpres, genFunc):
    (bestof, result) = timer.bestoftotal(func, _reps1=5, _reps=1000)
    print('%-9s: %.5f => [%s...%s]' %
          (func.__name__, bestof, result[0], result[-1]))
