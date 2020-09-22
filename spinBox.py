from tkinter import *
win = Tk()

win.title('SpinBar')
win.geometry("480x320")

#######################
#
# github.com/platinumg9
#
#######################

spin = Spinbox(win, from_=25, to = 50, width=5)
spin.grid(column=0, row=0)

spin2 = Spinbox(win, from_=1, to = 12, width=5)
spin2.grid(column=1, row=0)

win.mainloop()