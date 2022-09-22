"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
Ejemplo de estructuras condicionales Bifurcanciones (if)
"""

import os 
os.system('cls')




# declaracion de variables de trabajo 
MontoAumento = 0
PorAu = 0
# Entrada de datos via teclado

nombre = input("digite el nombre del Trabajador: ")
salario = int(input("Ingrese el salario actual del trabajador: "))

# seccion de comparacion de datos 
if salario < 10000:
    PorAu = "25%" #PorAu => porcentaje de aumento  
    MontoAumento = (salario * 25)/100 #MontoAumento => Contiene el monto a ser aumento en salario del 


if salario >= 11000 and salario < 20000:
        PorAu = "10%" 
        MontoAumento = (salario*10)/100

if salario >= 20000 and salario < 50000:
           PorAu = "5%" 
           MontoAumento = (salario*5)/100

if 110000 >= salario < 200000:
    print("Lo sentimos mucho, pero no tiene aumento....")


# Seccion de la aplicacion del aumento del salario 
SalAnt = salario # SalAnt => representa al salario anterior
salario = salario + MontoAumento

#seccion de la salida de la pantalla 
print(" Datos salariales del trabajador")
print("Nombre...................: "+ nombre)
print("Salario sin Aumento........:"+str(MontoAumento))
print("---------------------------------")
print ("Datos sobre el aumento de Salario aplicando ")
print("Porcentaje de aumento.....:"+PorAu)
print("Monto Aumento.....:"+str(MontoAumento))
print("Salario con el aumento...: ",salario)
print("--------------------------------------------------")






