"""
Record and processinformation about people.
Run this file directly to test its classes
"""
from classtools import AttrDisplay                          # Use generic display tool


class Person(AttrDisplay):                                  # Mix in a repr at this level
    """
    Generic class for a Person
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):                                    # Assume last is last
        """
        Return last name of a person
        """
        return self.name.split()[-1]

    def give_raise(self, percent):                          # Percent must be 0..1
        """
        Give raise to person's pay
        """
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    Inherit Person's attributes
    Customize give_raise method off Person class (overload it)
    """
    def __init__(self, name, pay=0):
        Person.__init__(self, name, "mgr", pay)             # Job name is implied

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


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
        