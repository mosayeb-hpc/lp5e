"""
File person.py (start)
Add record field initialization
Add defaults for constructor arguments
Add incremental self-test code
Allow this file to be imported as well as run/tested
Add methods to encapsulate operations for maintainability
Add __repr__ overload method for printing objects
"""
from __future__ import print_function


class Person:               # Start a class
    """
    Generic class for a Person
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        """
        Return last name of a person
        """
        return self.name.split()[-1]
    def give_raise(self, percent):
        """
        Give raise to person's pay
        """
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):              # Define a subclass of Person
    """
    Inherit Person's attributes
    Customize give_raise method off Person class (overload it)
    """
    def __init__(self, name, pay=0):
        Person.__init__(self, name, "mgr", pay)

    def give_raise(self, percent, bonus=.10):       # Redefine at this level
        Person.give_raise(self, percent + bonus)    # Call Person's version


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)
    tom = Manager("Tom Jones", 50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)
    print("--All Three--")
    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)
