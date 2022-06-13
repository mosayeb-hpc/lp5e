def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


def reciprocal(x):
    assert x != 0   # A generally useless assert!
    return 1 / x    # Pyhton checks for zero automatically
