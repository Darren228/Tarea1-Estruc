'''
crear llave primaria
'''
from dbm import _Database
import mysql.connector as mysql
db = mysql.connect(
    host = "Localhost",
    user = "root",
    passwd = "",
    Database = "DBPython"
)


conexion = db.cursor()

# Eliminar la tabla de usauarios 
# Drop table 
conexion.execute("Drop Table usuarios")

# Creacion de la tabla de los usuarios con la definicion de una llave primaria 
conexion.execute("CREATE TABLE usuarios (USU_USER varchar (30) not null PRIMARY KEY, USU_CLAV VARCHAR(20)not null) ")

conexion.close()
