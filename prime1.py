def prime(x):
    y = x // 2
    if x <= 1:
        return False
    else:
        for i in range(y, 1, -1):
            if x % i == 0:
                return False
        else:
            return True
