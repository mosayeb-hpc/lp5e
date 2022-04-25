import builtins

class ctester:
    def __init__(self, start) -> None:
        self.state = start
    def __call__(self, label=0):
        print(label, self.state)
        self.state += 1

def ftester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

def ltester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1
    state=[start]
    return nested

def makeopen(id):
    org = builtins.open
    def custom(*kargs, **pargs):
        print('Custom open call %r: ' % id, kargs, pargs)
        return org(*kargs, **pargs)
    builtins.open = custom

makeopen('Foo')
F = open('first.py')
F.read()
makeopen('Bar')
G = open('second.py')
G.read()
makeopen('Baz')
H = open('tester.py')

 

