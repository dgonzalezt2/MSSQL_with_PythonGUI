
import pyodbc
import funciones
try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-ETQSMPF\SQLEXPRESS;DATABASE=Proyecto;Trusted_Connection=yes;')

    cursor = connection.cursor();
    
    continuar = 'CONTINUAR'

    while continuar.upper() != 'SALIR':
        
        print("¿Qué desea realizar?")
        print("0. Salir")
        print("1. Registrar un estudiante")
        print("2. Modificar informacion de estudiante")
        print("3. Borrar un estudiante")
        print("4. Consultar libros por area")
        print("5. Mostrar deuda actual")
        print("6. Mostrar libros por editorial")
        print("7. Mostrar TODOS los libros disponibles")
        print("8. Solicitar prestamo de libro")
        print("9. Consultar areas disponibles")
        print("10. Devolver libros")
        print("11. Ver estudiantes en estado de mora")
        continuar = input()
        continuar = continuar.upper()
#----------------------------------------------------------------
        if continuar == "0":
            continuar = "SALIR"
#----------------------------------------------------------------
        if continuar == "1" or continuar == "REGISTRAR UN ESTUDIANTE":
            
            print("Ingrese la informacion del estudiante")
            
            id = str(input("id: "))
            CI = str(input("CI: "))
            nombre = str(input("nombre: "))
            Direccion = str(input("Direccion: "))
            NombreCarrera = str(input("Nombre de carrera: "))
            edad = str(input("edad: "))

            
            
            if nombre != "NULL":
                nombre = "'"+nombre+"'"
            if CI != "NULL":
                CI = "'"+CI+"'"
            if Direccion != "NULL":
                Direccion = "'"+Direccion+"'"
            

            funciones.registerEstudiante(id,CI, nombre, Direccion,NombreCarrera,edad)
        
#--------------------------------------------------------------------
        if continuar == "2" or continuar == "MODIFICAR ESTUDIANTE":
            id_Lector = str(input("id estudiante a modificar: "))
            print("¿Qué desea modificar?: " )
            print("1. CI")
            print("2. Nombre")
            print("3. Direccion")
            print("4. Carrera")
            print("5. Edad")
            print("6. Estado")

            if str(input()) == "1":

                funciones.updateEstudiante(id_Lector, "CI","'"+str(input("Ingrese el valor: "))+"'")
            elif str(input()) == "2":
    
                funciones.updateEstudiante(id_Lector, "nombre","'"+str(input("Ingrese el valor: "))+"'")
            elif str(input()) == "3":
    
                funciones.updateEstudiante(id_Lector, "direccion","'"+str(input("Ingrese el valor: "))+"'")
            elif str(input()) == "4":
    
                funciones.updateEstudiante(id_Lector, "id_carrera",str(input("Ingrese el valor: ")))
            elif str(input()) == "5":
    
                funciones.updateEstudiante(id_Lector, "edad",str(input("Ingrese el valor: ")))
            elif str(input()) == "6":
                funciones.updateEstudiante(id_Lector, "estado",str(input("Ingrese el valor: ")))
            


# -------------------------------------------------------------------
        if continuar == "3" or continuar == "BORRAR UN ESTUDIANTE":
            print("Ingrese el id del estudiante")
            

            id = str(input("id: "))
            
            funciones.deleteEstudiante(id)
#-------------------------------------------------------------------
        if continuar == "4" or continuar == "CONSULTAR LIBROS POR AREA":
            area = str(input("area a buscar: "))
            print("ID LIBRO  ||  TITULO  ||  EDITORIAL")
            funciones.searchArea(area)
#-----------------------------------------------------------------------
        if continuar == "5" or continuar == "MOSTRAR DEUDA":

            area = str(input("ID Estudiante: "))
            
            funciones.calcularDeuda(area)
#------------------------------------------------------------------------------
        if continuar == "8" or continuar == "SOLICITAR PRESTAMO DE LIBRO":
            estudiante = str(input("id estudiante: "))
            libro = str(input("id libro: "))
            funciones.prestamo(estudiante,libro)
            
#----------------------------------------   
        if continuar == "9" or continuar == "VER AREAS":
            funciones.seeAreas()


        if continuar == "10" or continuar == "Devolver libros":
            id_Lector= str(input("ID del lector: "))
            id_Libro= str(input("ID del libro: "))
            fecha = str(input("Fecha de préstamo (M/D/Y): "))


    print("SALIENDO...")
#-------------------------------------------------------------------

    


except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")
