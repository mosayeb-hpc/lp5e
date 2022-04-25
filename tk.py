import sys
from tkinter import Button, mainloop

x = Button(text='button', 
    command=lambda : sys.stdout.write('Spam\n'))
x.pack()
mainloop()

