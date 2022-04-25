def adder(x, y):
    return x + y


def adder1(*args):
    print('adder1', end=' ')
    if type(args[0]) == type(0):
        res = 0
    else:
        res = args[0][:0]
    for arg in args:
        res += arg
    return res


def adder2(*args):
    print('adder2', end=' ')
    # for prevent in-place change in args if args ar mutables
    args = args[:]
    sum = args[0]
    for arg in args[1:]:
        sum += arg
    return sum


def adder11(**kargs):
    print('adder11', end=' ')
    values = list(kargs.values())
    if type(values[0]) == type(0):
        sum = 0
    else:
        sum = values[0][:0]
    for val in values:
        sum += val
    return sum


def adder22(**kargs):
    print('adder22', end=' ')
    return adder2(*list(kargs.values()))


s = 'abcdefghijklmnopqrstuvwxyz'
d1 = dict(zip(s, range(10)))
d2 = dict(zip(s, ('foo', 'bar', 'baz')))
d3 = dict(zip(s, (['a', 'b'], ['c', 'd'], ['e', 'f'])))
print('d1 == ', d1, '\nd2 == ', d2, '\nd3 == ', d3)
print(adder11(**d1))
print(adder11(**d2))
print(adder11(**d3))
print(adder22(**d1))
print(adder22(**d2))
print(adder22(**d3))


for func in (adder2, adder1):
    print(func(*range(1, 10)))
    print(func('foo', 'bar', 'baz'))
    print(func(['a', 'b'], ['c', 'd'], ['e', 'f']))


print(adder(2, 3))
print(adder('foo', 'bar'))
print(adder(('a', 'b'), ('c', 'd')))
