"""
pybench_cases.py: Run pybench on a set of pythons and statements.
Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "C:\python27\python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py -3 pybench_cases.py -a -t" to trace command lines too.
"""

import pybench
import sys

pythons = [
    (1, 'python3'),
    (0, 'python2-jamesh.python'),
    (1, 'pypy3'),
    (0, 'pypy')
]

stmts = [
    (0, 0, "[x ** 2 for x in range(1000)]"),
    (0, 0, "res=[]\nfor x in range(1000):\n\tres.append(x ** 2)"),
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),
    (0, 0, "list(x ** 2 for x in range(1000))"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
    (0, 0, "s = '?'\nfor i in range(10000):\n\ts += '?'")
]

stmts1 = [
    (0, 0, "pass"),
    (0, 0, "pass"),
    (0, 0, "pass"),
    (0, 0, "pass"),
    (0, 0, "pass"),
    (0, 0, "pass")
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)
