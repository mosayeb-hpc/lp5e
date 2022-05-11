from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def method(self):
        print("in Super.method")        # Default behavior
    def delegate(self):         
        self.action()                   # Expected to be defined
    @abstractmethod
    def action(self):
        pass

class Inheritor(Super):                 # Inherit method verbatim
    pass

class Extender(Super):                  # Extend method behavior
    def method(self):
        print("starting Extender.method")
        Super.method(self)
        print("ending Extender.method")

class Replacer(Super):                  # Replace method completely
    def method(self):
        print("in Replacer.method")

class Provider(Super):                  # Fill in a required method
    def action(self):
        print("in Provider.action")

if __name__ == "__main__":
    for Klass in (Inheritor, Replacer, Extender):
        print('\n' + Klass.__name__ + '...')
        Klass().method()
    print('\n' + "Provider" + '...')
    Provider().delegate()
