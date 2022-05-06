# File person.py (start)
# Add record field initialization
# Add defaults for constructor arguments
# Add incremental self-test code
# Allow this file to be imported as well as run/tested
# Add methods to encapsulate operations for maintainability
# Add __repr__ overload method for printing objects

# File person-composite.py
# Embedding-based Manager alternative


class Person:               # Start a class
    def __init__(self, name, job=None, pay=0): 
        self.name = name
        self.job = job
        self.pay = pay

    def last_Name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=0.10):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.last_Name(), sue.last_Name())
    sue.give_raise(0.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(tom.last_Name())
    print(tom)
    print('--All three--')
    for obj in (bob, sue, tom):
        obj.give_raise(0.10)
        print(obj)
