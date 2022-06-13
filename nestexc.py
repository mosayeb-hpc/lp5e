def action2():
    print(1 + [])  # Generate TypeError


def action1():
    try:
        action2()
    except TypeError:       # Most recent matching try
        print('inner try')


try:
    action1()
except TypeError:           # Here, only if action1 re-raise
    print('outer try')

# Syntactic Nesting
try:
    try:
        action2()
    except TypeError:
        print('inner try')
except TypeError:
    print('outer try')
