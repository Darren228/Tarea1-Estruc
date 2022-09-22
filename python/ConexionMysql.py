"""
programa realiza una conexion a musql desde python
fecha.........: 29.03.2022
Autor.......: Darren De La O Gonzalez
"""
import os 
import mysql.connector as mysql



os.system('cls')

db=mysql.connect(
host= "localhost",
user= "root",
passwd="",
database = "DBPython"
)
print(db)

# Comando para cerrar la conexion a la mysql
comando = db.cursor()

comando.execute("CREATE TABLE usuarios (USU_USER varchar(30), USU_CLAV VARCHAR(20))")
