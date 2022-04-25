from __future__ import division, print_function, absolute_import
import sys

with open('tmp0.bin', 'wb') as F:
    F.write(b'foo' + b'bar' + b'baz' + b'\xc3\x84' + b'\n')

with open('tmp0.txt', 'w') as F:
    F.write('foo' + 'bar' + 'baz' + '\xc4' + '\n')

with open('tmp0.bin', 'rb') as F:
    print(F.read().decode())
