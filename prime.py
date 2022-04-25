from os import link


def prime(y=2):
    x = y // 2

    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')


def search(x, val):
    while x:
        if x[0] == val:
            print('found')
            break
        x = x[1:]
    else:
        print('NOT found')


def line_count(file):
    for i, line in enumerate(open(file)):
        pass
    return i+1


def tail(file='/home/mosayeb/.vimrc'):
    nlines = line_count(file)

    if nlines <= 10:
        for line in open(file):
            print(line.rstrip())
        return

    f = open(file)
    for i, x in enumerate(f):
        if i == nlines - 10:
            print(f.read())
