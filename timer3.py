"""
Same usage as timer2.py, but uses 3.X keyword-only default arguments
instead of dict pops for simpler code. No need to hoist range() out
of tests in 3.X: always a generator in 3.X, and this can't run on 2.X.
"""

import time, sys
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, _reps=1000, **kargs):
#    _reps = kargs.pop('_reps', 1000)    # Passed-in or default reps
    repslist = list(range(_reps))       # Hoist range out for 2.X lists
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, _reps=5, **kargs):
#    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best : best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _reps1=5, **kargs):
#    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))