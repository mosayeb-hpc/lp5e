import sys


def Bye():
    sys.exit(40)


try:
    Bye()
except:
    print('got it')
print('continuing')
