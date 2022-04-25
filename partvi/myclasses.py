class FirstClass:               # Define a class object
    def setdata(self, value):   # Define class's methods
        self.data = value       # self is the instance
    def display(self):
        print(self.data)        # self.data: per instance


class SecondClass(FirstClass):                   # Inherits setdata
    def display(self):                           # Changes display
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):               # Inherit from SecondClass
    def __init__(self, value):               # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other):                # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self):                       # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):                    # In-place change: named
        self.data *= other

class rec:
    pass


def uppername(x):
    return x.name.upper() # Still need a self argument (x)


def print_bases(x):
    st = [x.__class__]
    while st:
        cl = st.pop()
        print(cl)
        st.extend(cl.__bases__)

