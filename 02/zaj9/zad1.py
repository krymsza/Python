import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox

root = tk.Tk()

def mes(): 
    tk.messagebox.showinfo("wybrano: ", v.get())

def valPrint(p):  
    print(p.get())
    if(p.get() == 1):
        b1.configure(fg = "red")
    elif(p.get()==2):
        b1.configure(fg = "green")
    else:
        b1.configure(fg = "blue")

v = tk.IntVar()
b1 = tk.Button(root, text=" kolor ",command= mes )
b1.pack()
ttk.Radiobutton(root, text = " R ", variable = v, command = lambda:valPrint(v), value =1).pack()
ttk.Radiobutton(root, text = " G ", variable = v, command = lambda:valPrint(v), value =2).pack()
ttk.Radiobutton(root, text = " B ", variable = v, command = lambda:valPrint(v), value =3).pack()
root.mainloop()
