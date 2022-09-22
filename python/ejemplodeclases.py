"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
demuestra a definicion una clase en python 
"""
import os
from sqlite3 import adapt
os.system('cls')

class MiClase:
 # zona para definir atributos
 numeros = 123456

#  zona para definir metodos
def metodo1(self):
    return 'esto es un metodo simple'
    # fin metodo

# seccion de la rutina principa de la clase 

# zona donde se define una instancia o objeto de la clase 
ObjMiClase = MiClase()
# usando el metodo de la clase MiClase por medio del objeto MiCLase
print(ObjMiClase.metodo1())
print (ObjMiClase.numeros)

