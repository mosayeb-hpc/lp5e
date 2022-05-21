from __future__ import print_function
from ast import Call
import sys

if sys.version_info[0] == 3:
    from tkinter import Button, mainloop
else:
    from Tkinter import Button, mainloop


class Callback:
    def __init__(self, value):
        self.value = value

    def __call__(self):
        print('Spam %s' % self.value)
        self.value += 1


def func(value):
    def callback():
        print('Ham %s' % callback.state)
        callback.state += 1
    callback.state = value
    return callback

class Callback1:
    def __init__(self, value):
        self.value = value
    
    def change(self):
        print('eggs %s' % self.value)
        self.value += 1


c1 = Callback(0)
c2 = func(0)
c3 = Callback1(0)

x = Button(text='button1', command=c1)
y = Button(text="button2", command=c2)
z = Button(text="button3", command=c3.change)
a = Button(text="button4", command=lambda i=0: print('foo %s' % i))
x.pack()
y.pack()
z.pack()
a.pack()
mainloop()
