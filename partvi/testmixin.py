# File testmixin.py (2.X + 3.X)
"""
Generic lister mixin tester: similar to transitive reloader in
chapter 25, but passes a class object to tester (not function),
and testByName adds loading of both module and class by name
string here, in keeping with Chapter 31's factories pattern.
"""
import importlib


def tester(listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)


def testByName(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)


if __name__ == "__main__":
    testByName('listinstance', 'ListInstance', True)
    #testByName('listinherited', 'ListInherited', True)
    #testByName('listtree', 'ListTree', False)
