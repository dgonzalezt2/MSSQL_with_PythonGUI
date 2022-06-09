from re import L
from tkinter import *

from .consultar import consultar
from .consultarArea import consultarArea
from .consultarDisponibles import consultarDisponibles
from .consultarEditorial import consultarEditorial


def menuLibros():
    y2 = Frame()
    y2.config(background = "#213141")
    y2.place(x=0, y=0, width=500, height=1000)
    y3 = Label(y2, text="CONSULTAR LIBROS ",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=60)

    Button(y2, text='CONSULTAR POR AREA', width=50,padx = 10, pady = 10, bg="black", fg='white',command=consultarArea).place(x=70, y=130)
    Button(y2, text='CONSULTAR POR EDITORIAL', width=50,padx = 10, pady = 10, bg="black", fg='white',command=consultarEditorial).place(x=70, y=180)
    Button(y2, text='CONSULTAR LIBROS DISPONIBLES', width=50,padx = 10, pady = 10, bg="black", fg='white',command=consultarDisponibles).place(x=70, y=230)
    Button(y2, text='RETURN', width=40, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=115, y=280)