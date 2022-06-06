def tracer(func):
    def oncall(*args):
        oncall.call += 1
        print("Call %s to %s" % (oncall.call, func.__name__))
        return func(*args)
    oncall.call = 0
    return oncall


@tracer
def spam(a, b, c):
    return a + b + c


print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))
