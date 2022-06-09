from logging import root
from tkinter import *

def registro():
  def send_data():
    ID_info = str(ID.get())
    CI_info = str(CI.get())
    Nombre_info = str(Nombre.get())
    Direccion_info = str(Direccion.get())
    Carrera_info = str(Carrera.get())
    Edad_info = str(Edad.get())
    print(ID_info,"\t",CI_info,"\t",Nombre_info,"\t", Direccion_info,"\t", Carrera_info,"\t", Edad_info)
    

  #  Open and write data to a file
    file = open("user.txt", "a")
    file.write(ID_info)
    file.write("\t")
    file.write(CI_info)
    file.write("\t")
    file.write(Nombre_info)
    file.write("\t")
    file.write(Direccion_info)
    file.write("\t")
    file.write(Carrera_info)
    file.write("\t")
    file.write(Edad_info)
    file.write("\t\n")
    file.close()
    print(" NUEVO USUARIO. ID: {} | CI: {} | Nombre: {} | Direccion: {} Carrera: {} | Edad: {} |   ".format(ID_info,CI_info,Nombre_info,Direccion_info, Carrera_info,Edad_info ))
  
  #  Delete data from previous event
    ID_entry.delete(0, END)
    CI_entry.delete(0, END)
    Nombre_entry.delete(0, END)
    Direccion_entry.delete(0, END)
    Carrera_entry.delete(0, END)
    Edad_entry.delete(0, END)

  # Create new instance - Class Tk()  
  root = Tk()
  root.geometry("650x650")
  root.title('Registration Form')

  # Creating Sub-Title
  a = Label(root, text="Registration Form", bg='black', fg='white', width=20, font=("bold", 20))
  a.place(x=90, y=60)

  # Define Label Fields 
  Nombre_label = Label(text = "ID", bg = "#dde7ff")
  Nombre_label.place(x = 22, y = 70)
  Nombre_label = Label(text = "CI", bg = "#dde7ff")
  Nombre_label.place(x = 22, y = 130)
  Nombre_label = Label(text = "Nombre", bg = "#dde7ff")
  Nombre_label.place(x = 22, y = 190)
  Direccion_label = Label(text = "Direccion", bg = "#dde7ff")
  Direccion_label.place(x = 22, y = 250)
  Carrera_label = Label(text = "Carrera", bg = "#dde7ff")
  Carrera_label.place(x = 22, y = 310)
  Edad_label = Label(text = "Edad", bg = "#dde7ff")
  Edad_label.place(x = 22, y = 370)
  
  # Get and store data from users 
  ID = StringVar()
  CI = StringVar()
  Nombre = StringVar()
  Direccion = StringVar()
  Carrera = StringVar()
  Edad = StringVar()

  ID_entry = Entry(textvariable= ID, width = "40" )
  CI_entry = Entry(textvariable= CI, width = "40" )
  Nombre_entry = Entry(textvariable = Nombre, width = "40")
  Direccion_entry = Entry(textvariable = Direccion, width = "40")
  Carrera_entry = Entry(textvariable = Carrera, width = "40")
  Edad_entry = Entry(textvariable = Edad, width = "40")

  ID_entry.place(x = 22, y = 100)
  CI_entry.place(x = 22, y = 160)
  Nombre_entry.place(x = 22, y = 220)
  Direccion_entry.place(x = 22, y = 280)
  Carrera_entry.place(x = 22, y = 340)
  Edad_entry.place(x = 22, y = 400)
  
  # Submit Button and back Button
  submit_btn = Button(root,text = "Submit Info", width = "30", height = "2", command = send_data, bg = "#56cd92")
  submit_btn.place(x = 22, y =460)
    
  back_btn= Button(root,text= "Back", width = "30", height = "2", command = root.destroy, bg = "#cd5656") 
  back_btn.place(x = 22, y =520)

  # Imagen
  """ventana=Tk()
  imagen=PhotoImage(file="sql-server-1.png")
  fondo=Label(mywindow,image=imagen).place(x=70,y=220)
  """
  root.mainloop()

registro()