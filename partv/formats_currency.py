from __future__ import print_function   # 2.X
from formats import money as m
X = 54321.987

print(m(X), m(X, 0, ''))
print(m(X, currency=u'\xA3'), m(X, currency=u'\u00A5'))
print(m(X, currency=b'\xA3'.decode('latin-1')))

print(m(X, currency=u'\u20AC'), m(X, 0, b'\xA4'.decode('iso-8859-15')))
print(m(X, currency=b'\xA4'.decode('latin-1')))
