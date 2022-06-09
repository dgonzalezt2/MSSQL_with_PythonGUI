from asyncio.windows_events import NULL
from tkinter import *
from Database import funciones
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter import ttk

def registrarEstudiante():

    carrerasDict = {}
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="REGISTRAR ESTUDIANTE",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=60)

    # Creating FullName
    b = Label(y2, text="ID:", width=20, font=("bold", 12))
    b.place(x=75, y=130)
    # Creating Entry For FullName
    b1 = Entry(y2)
    b1.place(x=300, y=130)

    # Creating CI
    c = Label(y2, text="CI:", width=20, font=("bold", 12))
    c.place(x=75, y=180)
    # Creating Entry For CI
    c1 = Entry(y2)
    c1.place(x=300, y=180)

    # Creating NOMBRE
    d = Label(y2, text="NOMBRE:", width=20, font=("bold", 12))
    d.place(x=75, y=230)
    # Creating Entry For NOMBRE
    d1 = Entry(y2)
    d1.place(x=300, y=232)

    # Creating DIRECCION
    e = Label(y2, text="DIRECCION:", width=20, font=("bold", 12))
    e.place(x=75, y=280)
    # Creating Entry For DIRECCION
    e1 = Entry(y2)
    e1.place(x=300, y=280)

    # Creating NOMBRE CARRERA
    f = Label(y2, text="ID CARRERA:", width=20, font=('bold', 12))
    f.place(x=75, y=330)
    # Creating Entry For NOMBRE CARRERA

    # Combobox creation
    n = StringVar()
    monthchoosen = ttk.Combobox(y2, state="readonly", width = 20, textvariable = n)
    monthchoosen.place(x=300, y=332)
    # Adding combobox drop down list
    def getCarreras():
        res = funciones.selectCarrera()
        carrerasName=[]
        for i in res:
            if i[1] not in carrerasDict:
                carrerasDict[i[1]]=i[0]
            carrerasName.append(i[1])
        monthchoosen['values'] = carrerasName
    getCarreras()
    monthchoosen.current()

    # Creating Confirm EDAD
    g = Label(y2, text="EDAD:", width=20, font=('bold', 12))
    g.place(x=75, y=380)
    # Creating Entry For Confirm EDAD
    g1 = Entry(y2)
    g1.place(x=300, y=382)
    def callback():
        if(b1.get()=='' and n.get()==''):
            showwarning("Arquitectura empresarial", "ID y CARRERA son campos requeridos") 
        elif(b1.get()==''):
           showwarning("Arquitectura empresarial", "ID es un campo requerido") 
        elif(n.get()==''):
           showwarning("Arquitectura empresarial", "CARRERA es un campo requerido") 
        else:
            if(funciones.validarID(b1.get())):
                showwarning("Arquitectura empresarial",  f"El ID {b1.get()} ya se encuentra registrado") 
            else:
                dict = {
                    "ID":"'"+b1.get()+"'",
                    "CI":("'"+c1.get()+"'" if c1.get()!='' else "'NULL'"),
                    "NOMBRE":("'"+d1.get()+"'" if d1.get()!='' else "'NULL'"),
                    "DIRECCION":("'"+e1.get()+"'" if e1.get()!='' else "'NULL'"),
                    "CARRERA":"'"+carrerasDict[n.get()]+"'",
                    "EDAD":("'"+g1.get()+"'" if g1.get()!='' else "NULL")
                }
                try:
                    res = funciones.registerEstudiante(dict["ID"],dict["CI"], dict["NOMBRE"], dict["DIRECCION"],dict["CARRERA"],dict["EDAD"])
                    if(res["status"]==1):
                        showinfo("Arquitectura empresarial",  res["message"])
                        y2.destroy()
                except Exception as ex:
                    print(ex)
                    showerror("Arquitectura empresarial",  "Ocurrio un error al registrar estudiante")

    Button(y2, text='SUBMIT', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=420)


    Button(y2, text='RETURN', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=460)
