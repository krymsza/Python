# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:42:28 2018

@author: kat
"""

import tkinter as tk
class Cal():
    
    def __init__(self):
        self.wynik = 0
        self.current = ""
        self.new_num = True
        self.str_operacja= ""
        self.eq = False
        self.op_pending = False
        
    def wpisz(self, num):
        liczba1 = text_box.get()
        liczba2 = str(num)
        if(self.new_num):
            self.current = liczba2
            self.new_num = False
        else:
            if(liczba2 == "."):
                if(liczba2 in liczba1):
                    return
            self.current =  liczba1 + liczba2
        self.wyswietl(self.current)
        
    def wyswietl(self, liczba):
        text_box.delete(0, tk.END)
        text_box.insert(0, liczba)
        
    def podsumuj(self):
        self.eq = True
        if(self.op_pending == True):
            self.dzialanie()
        else:
            self.total = float(text_box.get())
        
    def dzialanie(self):
        self.current = float(self.current)
        if( self.str_operacja == 'add'):
            self.total = self.total + self.current
        elif( self.str_operacja == 'minus'):
            self.total = self.total - self.current    
        elif( self.str_operacja == 'divide'):
            self.total = self.total / self.current
        elif( self.str_operacja == 'multiply'):
            self.total = self.total * self.current
        
        self.new_num = True
        self.op_pending = False
        self.wyswietl(self.total)

    def operacja(self, op):
        self.current = float(self.current)
        if(self.op_pending):
            self.podsumuj()
        elif(not self.eq):
            self.total = self.current
            
        self.new_num = True
        self.op_pending = True
        self.str_operacja = str_operacja
        self.eq = False
        
    def clear(self):
        self.eq = False
        self.current = ""
        self.wyswietl(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0
        
        
calculator = Cal()
root = tk.Tk()

frame = tk.Frame(root, width=350, height=300, bg="", colormap="new")
frame.pack()
root.minsize(width=350, height =300)
root.maxsize(width=350, height=300)

root.title("calculator")
text_box = tk.Entry(frame, justify = tk.RIGHT, width = 25, font="Times 16 bold" )
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "")       
        
i = 0
numbers = "789456123"   
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(tk.Button(frame, height =2, width=2, padx=15, command = lambda x = numbers[i]:calculator.wpisz(x),text = numbers[i]))
        bttn[i]["bg"]= "white"
        bttn[i].grid(row = j, column = k)
        i += 1

bttn_0 = tk.Button(frame,height=2, width=2,padx=15, command = lambda:calculator.wpisz("0"), text = "0",bg="white")
div = tk.Button(frame,height=2, width=2,padx=15, command = lambda: calculator.operacja("divide"), text = "/",bg="pink")
mult = tk.Button(frame,height=2, width=2, padx=15, command =lambda: calculator.operacja("multiply")  , text = "*",bg="pink")
minus = tk.Button(frame,height=2, width=2, padx=15, command = lambda: calculator.operacja("minus"), text = "-",bg="pink")
add = tk.Button(frame,height=2, width=2, padx=15, command = lambda: calculator.operacja("add"), text = "+",bg="pink")
point = tk.Button(frame,height=2, width=2, padx=15, command = lambda: calculator.wpisz("."), text = ".",bg="pink")
clear = tk.Button(frame,height=2, width=2, padx=15, command = calculator.clear, text = "C",bg="white")
all_clear = tk.Button(frame,height=2, width=2, padx=15, command =calculator.all_clear, text = "AC",bg="white")
equals = tk.Button(frame,height=4, width=2 ,padx=15, command =calculator.podsumuj, text = "=",bg="yellow")


equals.grid(row = 3, column = 4, columnspan=1, rowspan=2)
bttn_0.grid(row = 4, column = 0)
point.grid(row = 4, column = 1)
add.grid(row = 4, column = 3)
minus.grid(row = 3, column = 3)
mult.grid(row = 2, column = 3)
div.grid(row = 1, column = 3)
clear.grid(row = 1, column = 4)
all_clear.grid(row = 2, column = 4)

root.mainloop()        
        
        
