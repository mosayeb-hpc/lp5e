class Adder:
    def __init__(self, start=[]):
        self.data = start

    def add(self, y):
        return "Not Implemented"

    def __add__(self, other):
        return self.add(other)


class ListAdder(Adder):
    def add(self, y):
        return self.data + y


class DictAdder(Adder):
    def add(self, y):
        d = self.data.copy()
        for key, value in y.items():
            if not key in self.data:
                d[key] = value
        return d


if __name__ == "__main__":
    x = Adder(1)
    print(x + 1)
    x = ListAdder([1])
    print(x + [2])
    x = DictAdder({1:1})
    print(x + {2:2})
