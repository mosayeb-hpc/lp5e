import builtins


class cMakeopen:
    def __init__(self, id) -> None:
        self.id = id
        self.orig = builtins.open
        builtins.open = self

    def __call__(self, *kargs, **pargs):
        print('Custom open call %r:' % self.id, kargs, pargs)
        return self.orig(*kargs, **pargs)


F = cMakeopen('Foo')
F('first.py')
G = cMakeopen('Bar')
