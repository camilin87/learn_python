#! /usr/bin/env python

import sys
import Tkinter


def button_1_click():
    print 'lolo'


main_form = Tkinter.Tk()

button_1 = Tkinter.Button(main_form, text='Send Data', command=button_1_click)
button_1.pack()

label_1 = Tkinter.Label(main_form, text='This sends us to the moon')
label_1.pack()

main_form.mainloop()
