from scramble import scramble

def permute1(seq):
    if not seq:
        return [seq]
    res = []

    for i in range(len(seq)):
        rest = seq[:i] + seq[i+1:]
        x = seq[i:i+1]
        for item in permute1(rest):
            res.append(x + item)
    return res

#print(permute1('12'))


def permute2(seq):
    if not seq:
        yield seq
    for i in range(len(seq)):
        rest = seq[:i] + seq[i+1:]
        for item in permute2(rest):
            yield seq[i:i+1] + item

#print(sorted(permute2('123')))

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def myper(seq):
    res = []

    for i in range(len(seq)):
        x = seq[i:i+1]
        rst = seq[:i] + seq[i+1:]
        #res.extend(x)
        for item in list(scramble(rst)):
            res.append(x + item)
    return res

#print(myper('abcde')) 

   

