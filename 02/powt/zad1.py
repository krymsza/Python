import tkinter as tk
#import tkFont as tkF
import tkinter.font as tkF
import tkinter.filedialog as tkf

def otworzPlik():
    file_path = tkf.askopenfilename()
    F = open(file_path,"r")
    okno.insert(tk.END,F.read())
    
def zapiszPlik():
    file_path = tkf.asksaveasfilename()
    filer = open(file_path,"w")
    filer.write(okno.get())
    
def powieksz():
    global font_size
    font_size+=1
    okno.config(font = tkF.Font(family="Helvetica",size= font_size,weight="bold")) 
    
def pomniejsz():
    global font_size
    font_size-=1
    okno.config(font = tkF.Font(family="Helvetica",size= font_size,weight="bold")) 
    

root = tk.Tk()
root.maxsize(width=500, height=600)
root.minsize(width=500, height=600)
root.title("Notatnik")
font_size = 16
default_font = tkF.Font(family="Helvetica",size = font_size,weight="bold")
root.option_add("*Font", default_font)
okno = tk.Text(root,height=50, width=30)
okno.grid(row=1,column=0,columnspan=4,sticky = tk.W+tk.E+tk.N)


otworzBt = tk.Button(root, text ="Otwórz Plik", font =(tkF.Font(family="Helvetica",size=10,weight="bold")), command = otworzPlik)
zamknijBt = tk.Button(root, text ="zapisz Plik", font =(tkF.Font(family="Helvetica",size=10,weight="bold")), command = zapiszPlik)
powiekszBt = tk.Button(root, text ="Powieksz", font =(tkF.Font(family="Helvetica",size=10,weight="bold")), command = powieksz)
pomniejszBt = tk.Button(root, text ="Pomniejsz", font =(tkF.Font(family="Helvetica",size=10,weight="bold")), command = pomniejsz)
otworzBt.grid(row = 0,column=0,sticky = tk.W+tk.E)
zamknijBt.grid(row = 0,column=1,sticky = tk.W+tk.E)
powiekszBt.grid(row = 0,column=2,sticky = tk.W+tk.E)
pomniejszBt.grid(row = 0,column=3,sticky = tk.W+tk.E)


root.mainloop()
