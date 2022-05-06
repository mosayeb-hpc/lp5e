# File person.py (start)
# Add record field initialization
# Add defaults for constructor arguments
# Add incremental self-test code
# Allow this file to be imported as well as run/tested
# Add methods to encapsulate operations for maintainability
# Add __repr__ overload method for printing objects

# File person-department.py
# Aggregate embedded objects into a composite

from ast import arg


class Person:               # Start a class
    def __init__(self, name, job=None, pay=0): 
        self.name = name
        self.job = job
        self.pay = pay
    def last_name(self):
        return self.name.split()[-1]
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def give_raise(self, percent, bonus=0.10):
        Person.give_raise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    def add_member(self, person):
        self.members.append(person)
    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)
    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == "__main__":
    bob = Person('Bob Smith')
    sue = Person("Sue Jones", job="dev", pay=100000)
    tom = Manager("Tom Jones", pay=50000)

    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raise(.10)
    development.show_all()
