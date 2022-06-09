from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning
from Database import funciones

def devolver():
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="DEVOLVER LIBRO",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=60)

    b = Label(y2, text="ID ESTUDIANTE:", width=20, font=("bold", 12))
    b.place(x=75, y=130)
    # Creating Entry For FullName
    b1 = Entry(y2)
    b1.place(x=300, y=130)

    # Creating CI
    c = Label(y2, text="ID LIBRO:", width=20, font=("bold", 12))
    c.place(x=75, y=180)
    # Creating Entry For CI
    c1 = Entry(y2)
    c1.place(x=300, y=180)

    def callback():
        try:
            res = funciones.devolverLibros(b1.get(),c1.get())
            if(res["status"]==1):
                showinfo("Arquitectura empresarial",  res["message"])
                y2.destroy()
            elif(res["status"]==0):
                showwarning("Arquitectura empresarial",  res["message"])
        except:
            showerror("Arquitectura empresarial",  "Ocurrio un error al realizar la devolucion")

    Button(y2, text='Submit', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=230)


    Button(y2, text='Return', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=280)