from tkinter import *
from  tkinter import ttk
from Database import funciones

def consultarDisponibles():
    y2 = Frame()
    y2.place(x=0, y=0, width=500, height=1000)
    y2.config(background = "#213141")
    y3 = Label(y2, text="LIBROS DISPONIBLES",bg='black', fg='white', width=25,font=("bold", 22))
    y3.place(x=40, y=40)
    
    Button(y2, text='RETURN', width=20, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=180, y=460)


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
    
    my_game['columns'] = ('ID', 'TITULO', 'EDITORIAL')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("ID",anchor=CENTER, width=80)
    my_game.column("TITULO",anchor=CENTER,width=200)
    my_game.column("EDITORIAL",anchor=CENTER,width=80)

    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("ID",text="ID",anchor=CENTER)
    my_game.heading("TITULO",text="TITULO",anchor=CENTER)
    my_game.heading("EDITORIAL",text="ID EDITORIAL",anchor=CENTER)

    def callback():
        try:
            for i in my_game.get_children():
                my_game.delete(i)
            cont = 0
            res = funciones.showLibros()
            for i in res:
                my_game.insert(parent='',index='end',iid=cont,text='',
                values=(i[0],i[1],i[2]))
                cont +=1
            my_game.pack()
        except Exception as ex:
            print(ex)
    Button(y2, text='BUSCAR', width=20, bg="#04d616", fg='white', command=callback).place(x=180, y=120)