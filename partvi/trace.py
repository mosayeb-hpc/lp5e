# File trace.py (2.X + 3.X)
from __future__ import print_function

class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: %s' % attrname)
        return getattr(self.wrapped, attrname)
    def __getitem__(self, index):
        item = self.wrapped[index]
        return item
    def __repr__(self):
        return '%s: %s' % (self.wrapped.__class__.__name__,self.wrapped)
