# imports
from tkinter import *
from tkinter import ttk

main_win = Tk()
main_win.geometry('400x400+800+50')
main_win.configure(
    background='#000000',
    bd=0,
)

button_1 = Button(
    main_win,
    background='brown',
    text='button_1',
    width=7,
    height=1
)

button_2 = Button(
    main_win,
    background='brown',
    text='button_2',
    width=14,
    height=1
)


button_1.grid(column=0, row=0)
button_2.grid(column=1, row=0)

main_win.mainloop()
