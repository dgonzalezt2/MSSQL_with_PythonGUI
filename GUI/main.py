from tkinter import *
from PIL import ImageTk, Image

from views.student import vistaPrincipal as vistaEstudiantes
from views.books import vistaPrincipal as vistaLibros
from views.multas import vistaPrincipal as vistaMultas
from views.about import about

root = Tk()
canvas = Canvas(root, bg="#213141", width=500, height=500)
canvas.pack()
root.geometry("500x500")
root.config(background = "#213141")
root.title('Base De Datos EAFIT')

# Creating Sub-Title
a = Label(root, text="BIENVENIDO", bg='black', fg='white', width=20, font=("bold", 20))
a.place(x=95, y=60)


# Creating Entry For FullName
Button(root, text='MENU DE ESTUDIANTE', width=50,padx = 10, pady = 10,bg="black", fg='white', command=vistaEstudiantes.menuEstudiante).place(x=70, y=130)

Button(root, text='MENU DE LIBROS', width=50,padx = 10, pady = 10,bg="black", fg='white', command=vistaLibros.menuLibros).place(x=70, y=180)

Button(root, text='MENU DE PRESTAMOS', width=50,padx = 10, pady = 10,bg="black", fg='white', command=vistaMultas.menuMulta).place(x=70, y=230)
Button(root,text= "SALIR", width = "30", height = "2", command = root.destroy, bg = "#cd5656", fg='white') .place(x = 140, y =280)


image = Image.open("sql-server.png")
resize_image = image.resize((80, 80))
 
img = ImageTk.PhotoImage(resize_image)
canvas.create_image(80, 450, image=img)

image2 = Image.open("eafit.png")
resize_image2 = image2.resize((100, 50))
 
img2 = ImageTk.PhotoImage(resize_image2)
canvas.create_image(420, 450, image=img2)

Button(root,text= "SALIR", width = "30", height = "2", command = root.destroy, bg = "#cd5656", fg='white').place(x = 140, y =280)
Button(root,text= "ACERCA DE", width = "30", height = "2", command = about.about, bg = "#cd5656", fg='white').place(x = 140, y =330)

# this will run the mainloop.
root.mainloop()
