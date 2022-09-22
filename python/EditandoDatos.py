# Este programa permite realizar la actualizacion de datos en tabla de usuarios en la base de datos 
import mysql.connector as mysql

db = mysql.connect(
    host = "Localhost",
    user = "root",
    passwd = "",
    Database = "DBPython"
)

conexion = db.cursor()

