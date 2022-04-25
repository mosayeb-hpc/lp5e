import copy


def sumrec(*args):
    if len(args) == 1: 
        return args[0]
    return func(*args)

def func(*args):
    return args[0] + sumrec(*args[1:])

def rec(L):
    if L and isinstance(L, list):
       return rec(L.pop(0)) + rec(L)
    elif L:
        return L
    else:
        return 0


def rec1(L):
    total = 0
    for x in L:
        if isinstance(x, list):
            total += rec1(x)
        else:
            total += x
    return total


def rec2(L):
    total = 0
    res = []
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            res.extend(x)
    return total + rec2(res[:]) if res else total


def bfstree(L):
    total = 0
    res = L[:]
    while res:
        start = res.pop(0)
        if not isinstance(start, list):
            total += start
        else:
            res.extend(start)
    return total

def dfstree(L):
    total = 0
    res = L[:]
    while res:
        end = res.pop()
        if not isinstance(end, list):
            total += end
        else:
            res.extend(end)
    return total


L = [1, [2, [3, 4], 5], 6, [7, 8]]
L1 = copy.deepcopy(L)
L2 = copy.deepcopy(L)
L3 = copy.deepcopy(L)
L4 = copy.deepcopy(L)

print(rec(L))
print(rec1(L1))
print(rec2(L2))
print(bfstree(L3))
print(dfstree(L4))

