def countdown(N):
    if N == 0:
        print('stop')
        return
    print(N, end=' ')
    countdown(N - 1)


def countdowngen(N):
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdowngen(N - 1):
            yield x