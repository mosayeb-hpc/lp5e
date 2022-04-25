import sys

def print3(*pargs, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)

    output = ''
    first = True
    for arg in pargs:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)