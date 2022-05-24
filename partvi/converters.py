# File converters.py
from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, data):
        print("<h1>%s<h1>" % data.rstrip())


if __name__ == "__main__":
    import sys
    file = "/home/mosayeb/computer/code/python/lp5e/partvi/trispam.txt"
    F = open(file)
    obj = Uppercase(F, sys.stdout)
    obj.process()
    F.seek(0)
    obj = Uppercase(F, HTMLize())
    obj.process()
    F.close()