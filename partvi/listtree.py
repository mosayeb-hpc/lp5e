#!python
# File listtree.py

class ListTree(object):
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + "{0}\n".format(attr)
            else:
                result += spaces + "{0}={1}\n".format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return "\n{0}<Class {1}, address {2}: (see above)>\n".format(
                dots, aClass.__name__, id(aClass))
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent + 4)
            return "\n%s<Class %s, address %s:\n%s%s%s>\n" % (
                dots,
                aClass.__name__,
                id(aClass),
                here,
                above,
                dots
            )

    def __str__(self):
        self.__visited = dict()
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return "<Instance of %s(%s), address %s:\n%s%s>" % (
            self.__class__.__name__,
            self._supers(),
            id(self),
            here,
            above
        )

    def _supers(self):
        return ', '.join(
            sup.__name__ for sup in self.__class__.__bases__)


if __name__ == "__main__":
    import testmixin
    testmixin.tester(ListTree)
