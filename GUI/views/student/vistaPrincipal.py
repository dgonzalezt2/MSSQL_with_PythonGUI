from tkinter import *
from .registrar import registrarEstudiante
from .editar import editarEstudiante
from .eliminar import eliminarEstudiante
def menuEstudiante():
    
    y2 = Frame()
    y2.config(background = "#213141")
    y2.place(x=0, y=0, width=500, height=1000)
    y3 = Label(y2, text="REGISTRAR ESTUDIANTE",bg='black', fg='white', width=25, font=("bold", 22))
    y3.place(x=40, y=60)
    #y3.pack(fill=X)
   
    Button(y2, text='CREAR ESTUDIANTE', width=50,padx = 10, pady = 10, bg="black", fg='white',command=registrarEstudiante).place(x=70, y=130)
    Button(y2, text='EDITAR ESTUDIANTE', width=50,padx = 10, pady = 10, bg="black", fg='white',command=editarEstudiante).place(x=70, y=180)
    Button(y2, text='BORRAR ESTUDIANTE', width=50,padx = 10, pady = 10, bg="black", fg='white',command=eliminarEstudiante).place(x=70, y=230)
    Button(y2, text='RETURN', width=40, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=115, y=280)