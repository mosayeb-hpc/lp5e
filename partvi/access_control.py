# File: access_control.py

from __future__ import print_function


class AccessControl:
    def __setattr__(self, attr_name, attr_value):
        if attr_name == 'age':
            self.__dict__['age'] = attr_value + 10
        else:
            raise AttributeError(attr_name + ' not allowed')


if __name__ == "__main__":
    X = AccessControl()
    X.age = 40
    print(X.age)
    X.name = 'Sue Jones'
