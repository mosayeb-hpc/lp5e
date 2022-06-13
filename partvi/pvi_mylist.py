class MyList:
    def __init__(self, start):
        self.wrapped = list(start)

    def __add__(self, other):
        return MyList(self.wrapped + other)

    __radd__ = __add__

    def __repr__(self):
        return repr(self.wrapped)

    def __mul__(self, time):
        return MyList(self.wrapped * time)

    def __getitem__(self, i):
        return self.wrapped[i]

    def __len__(self):
        return len(self.wrapped)

    def append(self, value):
        self.wrapped.append(value)

    def __getattr__(self, name):
        return getattr(self.wrapped, name)


if __name__ == "__main__":
    x = MyList([1, 2, 3])
    print(x + [4, 5])
    print([4, 5] + x)
    print(x[1])
    y = MyList(list('javiuuiyvdatdfwqeplv,[VM,OIJEH'))
    y.sort()
    print(y)
    z = MyList(x)
    print(z)
