func = lambda x: 2 ** x
S1 = range(1,4)
S2 = range(-1,-7, -1)

def mymap(func, seq):
    res = []
    for x in seq:
        res.append(func(x))
    return res


def myreduce(F, seq):
    res = seq[0]
    for x in seq[1:]:
        res = F(res, x)
    return res

# return generator
def mymap1(func, *seqs):
    return (func(*args) for args in zip(*seqs))


def myzip1(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

def myzip1gen(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

def mymapPadgen(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

def myzip1Alt(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

def mymapPadAlt(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    return (tuple(S[i] if len(S) > i else pad for S in seqs) for i in range(maxlen))

print(list(mymapPadAlt(S1, S2, pad=99)))
