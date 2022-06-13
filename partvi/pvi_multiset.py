from setwrapper import Set


class MultiSet(Set):
    """
    Inherits all Set names, but extends intersect and union to support
    multiple operands; note that "self" is still the first argument
    (stored in the *args argument now); also note that the inherited
    & and | operators call the new methods here with 2 arguments, but
    processing more than 2 requires a method call, not an expression;
    intersect doesn't remove duplicates here: the Set constructor does;
    """

    def intersect(self, *others):
        res = []
        for x in self:
            for y in others:
                if not x in y:
                    break
            else:
                res.append(x)
        return MultiSet(res)

    def union(*args):         # self is args[0]
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return MultiSet(res)


if __name__ == "__main__":
    x = MultiSet([1, 2, 3, 4])
    y = MultiSet([3, 4, 5])
    z = MultiSet([0, 1, 2])

    print(x | y)
