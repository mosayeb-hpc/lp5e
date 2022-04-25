x = 1
def f1(x):
    def f2():
        print(x)
    return f2

f1(2)()
