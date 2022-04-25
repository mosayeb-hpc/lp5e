# File person.py (start)
# Add record field initialization
# Add defaults for constructor arguments
# Add incremental self-test code
# Allow this file to be imported as well as run/tested
# Add methods to encapsulate operations for maintainability
# Add __repr__ overload method for printing objects

class Person:               # Start a class
    def __init__(self, name, job=None, pay=0): 
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[%s: %s, %s]' % (self.__class__.__name__
                ,self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == "__main__":
    foo = Person("Foo Smith")
    bar = Person('Bar Jones', job='dev', pay=100000)
    print(foo)
    print(bar)
    print(foo.lastName(), bar.lastName())
    bar.giveRaise(0.10)
    print(bar)
    baz = Manager('Baz Jones', 500000)
    baz.giveRaise(.10)
    print(baz.lastName())
    print(baz)
    print('--All three--')
    for obj in (foo, bar, baz):
        obj.giveRaise(0.10)
        print(obj)

