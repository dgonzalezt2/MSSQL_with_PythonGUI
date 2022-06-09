from tkinter import *
from Database import funciones
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import ttk

def editarEstudiante():

    def changeState(entryToMod,var):
        if var.get()==1:
            entryToMod.config(state='normal',bg='white', fg='black')
        elif var.get()==0:
            entryToMod.config(state='disable',bg='gray', fg='white')

    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="¿QUE DESEA MODIFICAR?",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=30)

    # Creating FullName
    a = Label(y2, text="ID:", width=20, font=("bold", 12))
    a.place(x=75, y=80)
    # Creating Entry For FullName
    a1 = Entry(y2)
    a1.place(x=300, y=80)

    def getUserInfo():
        if(a1.get()==''):
            showwarning("Arquitectura empresarial", f"Campo ID requerido")
        else:
            carrerasDict = {}
            res = funciones.consultarEstudiante(a1.get())
            if(res["status"]):
                # Creating FullName
                b = Label(y2, text="CI:", width=20, font=("bold", 12))
                b.place(x=75, y=180)
                # Creating Entry For FullName
                text = StringVar()
                text.set(res["data"][1])
                b1 = Entry(y2,state='disable', bg='gray', fg='white',textvariable = text)
                b1.place(x=300, y=180)
                # Button to enable or disable the input
                state1 = IntVar()
                Checkbutton(y2, onvalue=1, offvalue=0,variable=state1,command=lambda:[changeState(b1,state1)]).place(x=250, y=180)
                # Creating CI
                c = Label(y2, text="NOMBRE:", width=20, font=("bold", 12))
                c.place(x=75, y=230)
                # Creating Entry For CI
                text2 = StringVar()
                text2.set(res["data"][2])
                c1 = Entry(y2, state='disable', bg='gray', fg='white',textvariable = text2)
                c1.place(x=300, y=230)
                # Button to enable or disable the input
                state2 = IntVar()
                Checkbutton(y2, onvalue=1, offvalue=0,variable=state2,command=lambda:[changeState(c1,state2)]).place(x=250, y=230)
                # Creating NOMBRE
                d = Label(y2, text="DIRECCION:", width=20, font=("bold", 12))
                d.place(x=75, y=280)
                # Creating Entry For NOMBRE
                text3 = StringVar()
                text3.set(res["data"][3])
                d1 = Entry(y2, state='disable', bg='gray', fg='white',textvariable = text3)
                d1.place(x=300, y=280)
                # Button to enable or disable the input
                state3 = IntVar()
                Checkbutton(y2, onvalue=1, offvalue=0,variable=state3,command=lambda:[changeState(d1,state3)]).place(x=250, y=280)
                # Creating DIRECCION
                e = Label(y2, text="CARRERA:", width=20, font=("bold", 12))
                e.place(x=75, y=330)
                # Creating Entry For DIRECCION
                text4 = StringVar()
                text4.set(res["data"][4])
                e1 = Entry(y2, state='disable', bg='gray', fg='white',textvariable = text4)
                #e1.place(x=300, y=280)
                n = StringVar()
                monthchoosen = ttk.Combobox(y2, state="readonly", width = 20, textvariable = n)
                monthchoosen.place(x=300, y=330)
                # Adding combobox drop down list
                def getCarreras():
                    res = funciones.selectCarrera()
                    carrerasName=[]
                    cont = 0
                    pos = 0
                    for i in res:
                        if i[1] not in carrerasDict:
                            carrerasDict[i[1]]=i[0]
                            if(i[0]==text4.get()):
                                if(cont>0):
                                    pos = cont
                        carrerasName.append(i[1])
                        cont+=1
                    print(carrerasName,pos)
                    monthchoosen['values'] = carrerasName
                    return pos
                Carrera = getCarreras()
                monthchoosen.current(Carrera)
                # Button to enable or disable the input
                state4 = IntVar()
                Checkbutton(y2, onvalue=1, offvalue=0,variable=state4,command=lambda:[changeState(e1,state4)]).place(x=250, y=330)
                # Creating NOMBRE CARRERA
                f = Label(y2, text="EDAD:", width=20, font=('bold', 12))
                f.place(x=75, y=380)
                # Creating Entry For NOMBRE CARRERA
                text5 = StringVar()
                text5.set(res["data"][5])
                f1 = Entry(y2, state='disable', bg='gray', fg='white',textvariable = text5)
                f1.place(x=300, y=380)
                # Button to enable or disable the input
                state5 = IntVar()
                Checkbutton(y2, onvalue=1, offvalue=0,variable=state5,command=lambda:[changeState(f1,state5)]).place(x=250, y=380)


                def callback():
                    labeloptions = [("CI",b1),("NOMBRE",c1),("DIRECCION",d1),("EDAD",f1)]
                    if(a1.get()==''):
                        showwarning("Arquitectura empresarial", f"Campo ID requerido")
                    else:
                        if(funciones.validarID(a1.get())):
                            totalOps=0
                            opsCompleted=0
                            for i in labeloptions:
                                if i[1].get()!='' and i[1]['state']=='normal':
                                    totalOps+=1
                                    try:
                                        res = funciones.updateEstudiante(a1.get(), i[0],"'"+i[1].get()+"'")
                                        opsCompleted+=1
                                    except Exception as ex:
                                        print(ex)
                            try:
                                if(state4.get()==1):
                                    funciones.updateEstudiante(a1.get(), "id_carrera","'"+carrerasDict[n.get()]+"'")
                                    opsCompleted+=1
                                    totalOps+=1
                            except Exception as ex:
                                print(ex)
                            if(totalOps==opsCompleted):
                                showinfo("Arquitectura empresarial", "Actualizacion completada")
                            elif(opsCompleted<totalOps):
                                showwarning("Arquitectura empresarial", f"Se actualizaron {opsCompleted}/{totalOps} registros")
                            elif(totalOps==0 or opsCompleted==0):
                                showerror("Arquitectura empresarial", f"No se pudo realizar la operacion con exito")

                            y2.destroy()
                        else:
                            showwarning("Arquitectura empresarial", f"El estudiante con ID {a1.get()} no se encuentra registrado")

                Button(y2, text='SUBMIT', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=420)
            else:
                showwarning("Arquitectura empresarial", f"El estudiante con ID {a1.get()} no se encuentra registrado")
    Button(y2, text='BUSCAR', width=20, bg="#04d616", fg='white', command=getUserInfo).place(x=180, y=130)
    
    Button(y2, text='RETURN', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=460)
