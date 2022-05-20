# File: private.py

from __future__ import print_function


class PrivateExe(Exception):
    pass


class Privacy:
    def __setattr__(self, attr_name, attr_value):
        if attr_name in self.privates:
            raise PrivateExe(attr_name, self)
        else:
            self.__dict__[attr_name] = attr_value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


if __name__ == "__main__":
    x = Test1()
    y = Test2()

    x.name = 'Bob'
    y.name = 'Sue'
    print(x.name)

    y.age = 30
    #x.age = 40
    print(y.age)
