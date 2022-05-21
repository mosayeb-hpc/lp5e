# File: __bool.py

from __future__ import print_function

class C:
    def __bool__(self):
        print('in __bool__')
        return False