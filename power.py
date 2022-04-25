L = [2 ** x  for x in range(7)]
X = 5

if 2 ** X in L:
    print((2**X), 'found at index', L.index(2**X))
else:
    print(X, 'not found')