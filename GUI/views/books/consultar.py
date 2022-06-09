from tkinter import *

def consultar():
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y3 = Label(y2, text="CONSULTAR LIBROS", width=30, height=12, font=("bold", 22), anchor=CENTER)
    y3.pack(fill=X)
    
    Button(y2, text='RETURN', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=460)
