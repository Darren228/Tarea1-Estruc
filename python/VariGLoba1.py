"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
cambiando el valor asignado a una variable
"""
import os 
os.system('cls')
def valor_global():
    global vg  
    vg="este es el primer valor de la variable global"
    # fin de la funcion

def mostrar_variable_local():
    print(vg)
    # fin de la funcion
# main
vg="este dato fue asignado a la variable global desde la rutina principal del programa"
mostrar_variable_local()
print(vg)
