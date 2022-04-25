"""
"""
from __future__ import print_function, absolute_import
import sys, copy
import importlib

if sys.version_info.major == 3:
    from importlib import reload
else:
    from imp import reload


def myreload(*modules):
    visited = {}
    if not modules:
        return
    for module in modules:
        print('module:', module.__name__, 'reloaded')
        visited[module] = True
        dic = module.__dict__.copy()
        L = get_mod(dic)

        while L:
            mod = L.pop(0)
            if not mod in visited: 
                reload(mod)
                visited[mod] = True
                print('module:', mod.__name__, 'reloaded')
                L1 = get_mod(mod.__dict__)
                L.extend(L1)
        

def get_mod(dic):
    L = list()
    for k in dic:
        if type(dic[k]) == type(sys):
            L.append(dic[k])
    return L


if __name__ == '__main__':
    import reloadall
    name, args = sys.argv[0], sys.argv[1:]
    if not args:
        myreload(reloadall)
    else:
        L = list()
        for arg in args:
            L.append(importlib.import_module(arg))
        myreload(*L)









