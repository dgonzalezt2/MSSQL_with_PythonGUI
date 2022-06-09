from tkinter import *
from  tkinter import ttk
from Database import funciones
from tkinter.messagebox import showinfo, showwarning, showerror

def consultarEditorial():
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="LIBROS POR EDITORIAL",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=40)
    
    Button(y2, text='RETURN', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=460)
    
    # Creating FullName
    b = Label(y2, text="EDITORIAL:", width=20, font=("bold", 12))
    b.place(x=75, y=80)
    # Combobox creation
    n = StringVar()
    monthchoosen = ttk.Combobox(y2, state="readonly", width = 20, textvariable = n)
    monthchoosen.place(x=300, y=80)
    # Adding combobox drop down list
    def getEditorial():
        res = funciones.seeEditoriales()
        carrerasName=[]
        for i in res:
            carrerasName.append(i[0])
        monthchoosen['values'] = carrerasName
    getEditorial()
    monthchoosen.current()


    game_frame = Frame(y2)
    # cambiar ubicacion en y de la tabla
    game_frame.pack(pady=150)
    #scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(game_frame,orient='horizontal')
    game_scroll.pack(side= BOTTOM,fill=X)

    my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)
    
    #define our column
    
    my_game['columns'] = ('NOMBRE', 'IDLIBRO', 'TITULO')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("NOMBRE",anchor=CENTER, width=100)
    my_game.column("IDLIBRO",anchor=CENTER,width=80)
    my_game.column("TITULO",anchor=CENTER,width=180)

    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("NOMBRE",text="NOMBRE",anchor=CENTER)
    my_game.heading("IDLIBRO",text="ID LIBRO",anchor=CENTER)
    my_game.heading("TITULO",text="TITULO",anchor=CENTER)

    def callback():
        try:
            if(n.get() == ''):
                showwarning("Arquitectura empresarial", "Seleccione una editorial a buscar") 
            else:
                for i in my_game.get_children():
                    my_game.delete(i)
                cont = 0
                res = funciones.searchEditorial(n.get())
                for i in res:
                    my_game.insert(parent='',index='end',iid=cont,text='',
                    values=(i[0],i[1],i[2]))
                    cont +=1
                if(cont==0):
                    showinfo("Arquitectura empresarial", "No hay libros en esta editorial")
                my_game.pack()
        except Exception as ex:
            showerror("Arquitectura empresarial", "Ocurrio un error")
    Button(y2, text='BUSCAR', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=120)