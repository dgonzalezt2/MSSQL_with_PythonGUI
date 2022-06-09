from tkinter import *
from  tkinter import ttk
from Database import funciones

def multa():
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="ESTUDIANTES EN MORA",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=40)
    
    Button(y2, text='Return', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=460)


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
    
    my_game['columns'] = ('IDLECTOR', 'NOMBRE', 'DEUDA')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("IDLECTOR",anchor=CENTER, width=80)
    my_game.column("NOMBRE",anchor=CENTER,width=200)
    my_game.column("DEUDA",anchor=CENTER,width=80)

    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("IDLECTOR",text="ID LECTOR",anchor=CENTER)
    my_game.heading("NOMBRE",text="NOMBRE",anchor=CENTER)
    my_game.heading("DEUDA",text="DEUDA ($COP)",anchor=CENTER)

    def callback():
        try:
            for i in my_game.get_children():
                my_game.delete(i)
            cont = 0
            res = funciones.verEstudiantesEnMora()
            for i in res:
                my_game.insert(parent='',index='end',iid=cont,text='',
                values=(i[0],i[1],i[2]))
                cont +=1
            my_game.pack()
        except Exception as ex:
            print(ex)
    Button(y2, text='Buscar', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=120)