import pyodbc
def connect():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-ETQSMPF\SQLEXPRESS;DATABASE=Proyecto;Trusted_Connection=yes;')
        #print("Conexión exitosa.")
        cursor = connection.cursor()
        return cursor

    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
   