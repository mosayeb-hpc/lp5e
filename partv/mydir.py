#!/usr/bin/env python2
"""
mydir.py: a module that lists the namespaces of other modules
"""
from __future__ import print_function, absolute_import
import sys


sep = '-'
seplen = 60


def listing(mod, verbose=True):
    sepline = sep * seplen
    dic = dict()
    try:
        dic = mod.__dict__
    except:
        print('please send a moudule name')
        return

    if verbose:
        print(sepline)
        print('module:', dic.get('__name__'), end=' ') 
        print('file:',  dic.get('__file__'))
        print(sepline)
    
    i = 0
    for k in sorted(dic.keys()):
        print('%03d) %s' % (i, k), end=' ')
        if k.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(mod, k))
        i += 1

    if verbose:
        print(sepline)
        print('%s has %d names' % (dic.get('__name__'), i))
        print(sepline)



if __name__ == '__main__':
#    main = sys.modules['__main__']
    import mydir
    listing(mydir)

