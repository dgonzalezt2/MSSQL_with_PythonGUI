from tkinter import *
from Database import funciones
from tkinter.messagebox import showinfo, showwarning, showerror

def eliminarEstudiante():
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="ELIMINAR USUARIO",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=60)

    # Creating FullName
    b = Label(y2, text="ID ESTUDIANTE:", width=20, font=("bold", 12))
    b.place(x=75, y=130)
    # Creating Entry For FullName
    b1 = Entry(y2)
    b1.place(x=300, y=130)

    def callback():
        try:
            res = funciones.deleteEstudiante(b1.get())
            if(res["status"]==1):
                showinfo("Arquitectura empresarial", res["message"])
            y2.destroy()
        except Exception as ex:
            showinfo("Arquitectura empresarial", "Ocurrio un error al elimiar el estudiante")

    Button(y2, text='SUBMIT', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=180)


    Button(y2, text='RETURN', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=230)
