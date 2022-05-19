# File: empty.py

from __future__ import print_function


class Empty:
    def __getattr__(self, attr_name):
        if attr_name == 'age':
            return 40
        else:
            raise AttributeError(attr_name)


if __name__ == "__main__":
    X = Empty()
    print(X.age)
    print(X.name)
