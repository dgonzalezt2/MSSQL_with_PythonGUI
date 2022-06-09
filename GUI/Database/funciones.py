from .conexion import connect
def registerEstudiante(id_Lector,CI,Nombre, direccion,id_carrera,edad):
    try:
        cursor=connect()
        cursor.execute("Insert into Estudiante values("+id_Lector+","+CI+","+Nombre+","+direccion+","+id_carrera+","+edad+" )")
        cursor.commit()
        return {"status":1,"message":"Se registro correctamente"}
    except Exception as ex:
        print("funciones")
        print("Error durante la creación de estudiante: {}".format(ex))

def validarID(ID):
    try:
        cursor=connect()

        cursor.execute("select id_Lector from Estudiante where id_Lector = "+ID)

        row = cursor.fetchall()

        if len(row) == 0:
            return False
        else:
            return True
    except Exception as ex:
        print("Error al validar: {}".format(ex))

def deleteEstudiante(id_Lector):
    try:
        cursor=connect()
        cursor.execute("delete from Estudiante where id_Lector = "+ str(id_Lector))
        cursor.commit()
        print("Estudiante eliminado con éxito")
        return {"status":1,"message":"Se elimino el estudiante correctamente"}
    except Exception as ex:
        print("Error durante la creación de estudiante: {}".format(ex))
        return {"status":-1,"message":ex}

    
def updateEstudiante(id_Lector, atributo,modificado):
    try:
        cursor=connect()
        
        cursor.execute("update Estudiante SET [" 
                        +atributo+"] = "+modificado+ " WHERE [id_Lector] =" +id_Lector)
        
        cursor.commit()
        return {"status":1,"message":"Se edito el estudiante correctamente"}
       
        print("Estudiante modificado con éxito")
    except Exception as ex:
        
        print("Error durante la actualización de estudiante: {}".format(ex))

def searchArea(desc_area):
    try:
        cursor=connect()
        
        cursor.execute("sELECT l.id_Libro, l.titulo, (select e.nombre_editorial from Editoriales e where e.id_editorial = l.id_editorial) "+
                        "fROM Libro l "+
                        "where l.AREA = (select a.AREA from Areas a where DESCRIPCION_AREA LIKE '"+desc_area+"')")
        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list
    
    except Exception as ex:
        
        print("Error en la búsqueda de libros: {}".format(ex))

def selectCarrera():
    try:
        cursor=connect()

        cursor.execute("select * "+
                        "from Carreras")
        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list

    except Exception as ex:

        print("Error en la búsqueda de carreras: {}".format(ex)) 
def showLibros():
    try:
        cursor=connect()

        cursor.execute("Select id_libro, titulo, area "+
                        "from Libro ")
        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list

    except Exception as ex:

        print("Error en la búsqueda de libros: {}".format(ex))

def searchEditorial(nom_editorial):
    try:
        cursor=connect()

        cursor.execute("sELECT e.nombre_editorial, id_libro, titulo "+
                        "from Editoriales e, Libro l "+
                        "where e.id_editorial = l.id_editorial and e.nombre_editorial LIKE '"+nom_editorial+"'")

        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list

    except Exception as ex:
        print("Error en la búsqueda de libros: {}".format(ex))

def seeEditoriales():
    try:
        cursor=connect()

        cursor.execute("select nombre_editorial from Editoriales")

        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list

    except Exception as ex:

        print("Error en la búsqueda de prestamos: {}".format(ex))

def seeAreas():
    try:
        cursor=connect()
        
        cursor.execute("select * from Areas")

        
        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list
       
    except Exception as ex:
        
        print("Error en la búsqueda de áreas: {}".format(ex))


def realizarPrestamo(id_lector, id_libro):
    try:
        cursor=connect()
        cursor.execute("select(datediff(day,p.fecha_prestamo, getdate())), id_Lector "+
                        "from Prestamo p "+
                        "where devuelto = 0 and id_Lector = "+id_lector+" and (select	(datediff(day,p.fecha_prestamo, getdate())))> 15")
        
        
        row = cursor.fetchone()
        
        if row != None:
            
            if int(row[0]) > 15:
                return {"status":0,"message":"No se puede realizar el prestamo, debe libros"}
            else:
                
                cursor.execute("Insert into Prestamo values("+id_lector+","+id_libro+",GETDATE(), 0 ,null,0)")
                cursor.commit()
                return {"status":1,"message":"Prestamo realizado"}
        else:
            cursor.execute("Insert into Prestamo values("+id_lector+","+id_libro+",GETDATE(), 0 ,null,0)")
            cursor.commit()
            return {"status":1,"message":"Prestamo realizado"}
    except Exception as ex:
        return {"status":-1,"message":f"Error en el prestamo de libros: {ex}"}

def devolverLibros(id_lector, id_libro):
    try:
        cursor=connect()

        cursor.execute("select DATEDIFF (DAY, (sELECT fecha_prestamo "+
                        "from Prestamo "+
                        "where id_Lector = '"+id_lector+"' and id_Libro = '"+id_libro+"'), GETDATE()) as resultado")

        fedif = cursor.fetchone()[0]
        if fedif != None:
            if int(fedif) > 15:
                deuda = (int(fedif)-15)*1000
                cursor.execute("update Prestamo SET devuelto = 1, fecha_Devolucion = GETDATE(), valor_multa = "+str(deuda)+" WHERE [id_Lector] ='" +str(id_lector)+"' and [id_libro] = '"+str(id_libro)+"'" )
                cursor.commit()
                return {"status":0,"message":f"Gracias por devolver el libro, debe pagar una mora de {str(deuda)} COP"}
            else:
                cursor.execute("update Prestamo SET devuelto = 1, fecha_Devolucion = GETDATE(), valor_multa = 0  WHERE [id_Lector] ='" +str(id_lector)+"' and [id_libro] = '"+str(id_libro)+"'" )
                cursor.commit()
                return {"status":1,"message":"¡Gracias por devolver el libro a tiempo!"}
        else:
            return {"status":0,"message":"No se ha realizado el prestamo de este libro por el estudiante..."}

    except Exception as ex:
        return {"status":-1,"message":f"Error en el prestamo de libros: {ex}"}
        
def verEstudiantesEnMora():
    try:
        cursor=connect()

        cursor.execute("select e.id_Lector as  id, e.nombre as nombre,sum(a.multa)/2 "+
                        "from( "+
                        "select (((select(datediff(day,p.fecha_prestamo, getdate())))-15)*1000) as multa "+
                        "from Prestamo p, Estudiante e "+
                        "where p.id_Lector = e.id_Lector and p.devuelto=0 and  ((select(datediff(day,p.fecha_prestamo, getdate()))) >15) ) a, "+
                        "Prestamo p, Estudiante e "+
                        "where  p.id_Lector = e.id_Lector and p.devuelto=0 and  ((select(datediff(day,p.fecha_prestamo, getdate()))) >15) "+
                        "group by e.id_Lector, e.nombre ")
        row_to_list = []
        for row in cursor:
            row_to_list.append([elem for elem in row])
        return row_to_list

    except Exception as ex:

        return {"status":-1,"message":f"Error el busqueda de estudiantes en mora: {ex}"}

def consultarEstudiante(ID):
    try:
        cursor=connect()

        cursor.execute("select * from Estudiante where id_Lector = "+ID)

        row = cursor.fetchall()

        if len(row) == 0:
            return {"status":False,"data":[]}
        else:
            return {"status":True,"data":row[0]}




    except Exception as ex:

        print("Error durante la consulta de estudiante: {}".format(ex))