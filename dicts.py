def copyDict(dict1):
    d1 = dict()
    for k, v in dict1.items():
        d1[k] = v
    return d1


def addDict(dict1, dict2):
    new = dict()
    for k in dict1:
        new[k] = dict1[k]
    for k in dict2:
        new[k] = dict2[k]
    return new


def adder(*pargs):
    """
    return sum of integers or concatenated sequences
    or merged dictionaries
    """
    if isinstance(pargs[0], int):
        sum = 0
    elif isinstance(pargs[0], dict):
        new = {}
        for d in pargs:
            new = addDict(new, d)
        return new
    else:
        sum = pargs[0][:0]

    for arg in pargs:
        sum += arg
    return sum


d1 = {1: 1, 2: 2}
d2 = copyDict(d1)

print(d1, d2)
d2[2] = '?'
print(d1, d2)

print(addDict(d1, d2))
print(addDict(d2, d1))  # order of d1, d2 arguments matter!

s1, s2, s3 = 'foo', 'bar', 'baz'
l1, l2, l3 = [1, 2], [3, 4], [5, 6]
a, b, c = 1, 2, 3
d1 = dict(zip('ab', '12'))
d2 = dict(zip('cd', '34'))
d3 = dict(zip('ef', '56'))

print(adder(a, b, c))
print(adder(s1, s2, s3))
print(adder(l1, l2, l3))
print(adder(d1, d2, d3))
