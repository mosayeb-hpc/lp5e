def f1(a, b): print(a, b)                   # normal args
def f2(a, *b): print(a, b)                  # positional varargs
def f3(a, **b): print(a, b)                 # keywordvarargs
def f4(a, *b, **c): print(a, b, c)          # mixed mode
def f5(a, b=2, c=3): print(a, b, c)         # defaults
def f6(a, b=2, *c): print(a, b, c)          # defaults and positional varargs
