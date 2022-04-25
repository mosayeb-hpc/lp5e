# File person.py (start)
# Add record field initialization
# Add defaults for constructor arguments
# Add incremental self-test code
# Allow this file to be imported as well as run/tested
# Add methods to encapsulate operations for maintainability
# Add __repr__ overload method for printing objects

# File person-department.py
# Aggregate embedded objects into a composite

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
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == "__main__":
    foo = Person("Foo Smith")
    bar = Person('Bar Jones', job='dev', pay=100000)
    baz = Manager('Baz Jones', 50000)

    development = Department(foo, bar)
    development.addMember(baz)
    development.giveRaise(.10)
    development.showAll()
