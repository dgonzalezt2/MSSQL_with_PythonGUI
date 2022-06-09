from tkinter import *
from .multas import multa
from .solicitarPrestamo import prestamo
from .devolverLibro import devolver

def menuMulta():
    y2 = Frame()
    y2.config(background = "#213141")
    y2.place(x=0, y=0, width=500, height=1000)
    y3 = Label(y2, text="CONSULTAR PRESTAMOS ",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=60)

    Button(y2, text='SOLICITAR PRESTAMO', width=50,padx = 10, pady = 10, bg="black", fg='white',command=prestamo).place(x=70, y=130)
    Button(y2, text='DEVOLVER LIBRO', width=50,padx = 10, pady = 10, bg="black", fg='white',command=devolver).place(x=70, y=180)
    Button(y2, text='ESTUDIANTES EN MORA', width=50,padx = 10, pady = 10, bg="black", fg='white',command=multa).place(x=70, y=230)
    Button(y2, text='RETURN', width=40, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=115, y=280)