#! /usr/bin/env python

import sys
import time
import Tkinter


def button_1_click():
    label_1['text'] = 'milliseconds {0}'.format(int(time.time() * 1000))


main_form = Tkinter.Tk()
#main_form['height'] = 

button_1 = Tkinter.Button(main_form, text='Send Data', command=button_1_click)
button_1.pack()

label_1 = Tkinter.Label(main_form, text='This sends us to the moon')
#label_1['height'] = 100.0
label_1.pack()

main_form.mainloop()
