#programa para la administracion de partes 
from tkinter import *
from tkinter import messagebox
from dbSQLite import Database
import os 
os.system('cls')

db= Database ('Soda.db')
import sqlite3

class Database:
    def __init__(self, dbSQLite):
        self.conn= sqlite3.connect(dbSQLite)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS partes(id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()


#Fin del metodo principal del python

#metodo de consulta de los datos de la tabla partes 
def fetch(self):
    self.cur.execute("Select * from partes")
    rows = self.cur.fetchall()
    return rows
#Fin del metodo de consulta de datos 

#metodo de insersion de datos a la tabla
def insert(self, part , customer,retailer, price):
    self.cur.execute("Insert Into partes values (null,", (part, customer,retailer,price))
    self.conn.commit()
#fin del metodo de insersion 

#metodo de eliminacion de datos a la tabla 
def remove(self, id):
    self.cur.execute("delete from partes where id=?",(id,))
    self.conn.commit()
#fin del  metodo de eliminacion 

#metodo de actualizacion de datos a la tabla 
def update(self,id, part, customer,retailer,price):
    self.cur.execute("Update partes",(part, customer,retailer,price))
    self.conn.commit()
#fin del metodo de actuacion 

def __del__(self):
    self.conn.close()
#Fin metodo cierrre conexion con la base 

#datos temporales de iniciacion de la aplicacion 
db = Database('tienda.db')# Esta linea crea la base de datos para SQLite3
db.insert("4GB DDR4 Ram", "John Doe", "microcenter","160")

