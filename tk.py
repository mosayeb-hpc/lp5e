import sys

if sys.version_info[0] == 3:
    from tkinter import Button, mainloop
else:
    from Tkinter import Button, mainloop


x = Button(text='button', 
    command=lambda : sys.stdout.write('Spam\n'))
x.pack()
mainloop()

