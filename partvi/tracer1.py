class tracer:
    def __init__(self, func):
        self.call = 0
        self.func = func

    def __call__(self, *args):
        self.call += 1
        print("Call %s to %s" % (self.call, self.func.__name__))
        return self.func(*args)


@tracer
def spam(a, b, c):
    return a + b + c


print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))
