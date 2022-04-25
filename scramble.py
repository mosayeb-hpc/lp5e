def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

def tester(func, items, trace=True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*args)))