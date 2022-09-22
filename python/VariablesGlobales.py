"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
Ejemplo de variables globales
"""
import os 
os.system('cls')
# Programa que realiza la demostracion de las variables globales
V1 = 35
V2 = 10

# Funcion sumar
def sumar():
    # definiendo las variables locales 
    V1= 21
    V2= 12
    print(V1 + V2)
    # fin funcion

# main
sumar()
print(V1,V2)

