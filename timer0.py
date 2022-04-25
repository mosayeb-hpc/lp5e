import time

def timer(func, *args):
    start = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
    for i in range(1000):
        func(*args)
    return time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID) - start