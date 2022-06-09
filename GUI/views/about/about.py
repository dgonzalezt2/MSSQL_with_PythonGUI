from tkinter import *
from PIL import ImageTk, Image

def about():
    
    y2 = Frame()
    canvas = Canvas(y2, bg="#213141", width=500, height=500)
    canvas.pack()
    y2.config(background = "#213141")
    y2.place(x=0, y=0, width=500, height=1000)
    y3 = Label(y2, text="INTEGRANTES",bg='black', fg='white', width=25, font=("bold", 22))
    y3.place(x=40, y=60)
    
    Button(y2, text='ANDRES LEONARDO ROJAS PEÑA', width=50,padx = 10, pady = 10, bg="black", fg='white').place(x=70, y=130)
    Button(y2, text='DANIEL PINEDA VELEZ', width=50,padx = 10, pady = 10, bg="black", fg='white').place(x=70, y=180)
    Button(y2, text='DAVID GONZALEZ TAMAYO', width=50,padx = 10, pady = 10, bg="black", fg='white').place(x=70, y=230)
    Button(y2, text='HOBARLAN UPARELA ARROYO', width=50,padx = 10, pady = 10, bg="black", fg='white').place(x=70, y=280)
    Button(y2, text='JUAN ESTEBAN CASTRO GARCIA', width=50,padx = 10, pady = 10, bg="black", fg='white').place(x=70, y=330)

    image = Image.open("sql-server.png")
    resize_image = image.resize((80, 80))
 
    img = ImageTk.PhotoImage(resize_image)
    canvas.create_image(80, 450, image=img)

    image2 = Image.open("eafit.png")
    resize_image2 = image2.resize((100, 50))
 
    img2 = ImageTk.PhotoImage(resize_image2)
    canvas.create_image(420, 450, image=img2)
 
    
    Button(y2, text='RETURN', width=40, bg="#cd5656", fg='white', command=lambda:[y2.destroy()]).place(x=115, y=380)
    y2.mainloop()