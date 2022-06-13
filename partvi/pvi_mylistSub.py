from pvi_mylist import MyList

class MyListSub(MyList):
    numAdd = 0
    def __init__(self, start):
        self.numAddIns = 0
        MyList.__init__(self, start)

    def __add__(self, other):
        print('Adding %s to %s' % (self.wrapped, other))
        MyListSub.numAdd += 1
        self.numAddIns += 1
        return MyList.__add__(self, other)

    __radd__ = __add__

    def status(self):
        return self.numAdd, self.numAddIns

if __name__ == "__main__":
    x = MyListSub([1, 2, 3])
    print(x + [4, 5])
    print([4, 5] + x)
    print(x[1])
    y = MyListSub(list('javiuuiyvdatdfwqeplv,[VM,OIJEH'))
    y.sort()
    print(y)
    z = MyListSub(x)
    print(z)
    l = [11,22]
    print(x+l, l+x)
