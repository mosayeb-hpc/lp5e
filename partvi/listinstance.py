#!python
# File listinstance.py (2.X + 3.X)
from __future__ import print_function


class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; display instance attrs only; self is a
    instance of lowest class; __X names avoid clashing with client's attrs
    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )
if __name__=="__main__":
    import testmixin
    testmixin.tester(ListInstance)