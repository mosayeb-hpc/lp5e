"""
classtree.py: Climb inheritance tree using namepace links,
displaying higher superclasses with indentation for height
"""

def class_tree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        class_tree(supercls, indent + 3)

def instanse_tree(inst):
    print('Tree of %s' % inst)
    class_tree(inst.__class__, 3)

def self_test():
    class A:        pass
    class B(A):     pass
    class C(A):     pass
    class D(B, C):  pass
    class E:        pass
    class F(D, E):  pass
    instanse_tree(B())
    instanse_tree(F())

if __name__ == "__main__": self_test()