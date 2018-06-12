# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:54:29 2018

@author: kat
"""

import tkinter as tk
import tkinter.messagebox
import time

root= tk.Tk()
root.minsize(width=50, height = 50)
root.maxsize(width=50, height = 50)

def start(czas):
    czas = int(val.get())
    while(czas>0):
        print( " odliczam %s"%czas )
        time.sleep(1)
        czas = czas - 1
    if(czas == 0):
        tkinter.messagebox.showinfo("Info", "koniec odliczania")


def callback():
    print(val.get())

val = tk.Entry()
val.pack()
val.focus_set()
str_czas = val.get()

bt_start = tk.Button(root, text="start", command=lambda:start(str_czas))
bt_start.pack()

root.mainloop()
