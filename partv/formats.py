"""
File: formats.py (2.X and 3.X)
Various specialized string display formatting utilities.
Test me with canned self-test or command-line arguments.
To do: add parens for negative money, add more features.
"""


def commas(N):
    """
    Format positive integer-like N for display with
    commas between digit groupings: "xxx,yyy,zzz".
    """

    res = ''
    s = str(N)
    while s:
        s, last3 = s[:-3], s[-3:]
        if not res:
            res = last3
        else:
            res = last3 + ',' + res
    return res


def money(N, numwidth=0, currency='$'):
    """
    Format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: "$ -xxx,yyy.zz".
    numwidth=0 for no space padding, currency='' to omit symbol,
    and non-ASCII for others (e.g., pound=u'\xA3' or u'\u00A3').
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    r = str(int(N))
    r = commas(r)
    f = ('%.2f' % N)[-3:]
    s = '%s%s%s' % (sign, r, f)
    return '%s%*s' % (currency, numwidth, s)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print(money(-1234567.9876, 15, u'\u00a3'))
    else:
        N = float(sys.argv[1])
        numwith = int(sys.argv[2])
        print(money(N, numwith))
