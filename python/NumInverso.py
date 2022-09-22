""" 
Universidad politecnica de Costa Rica - Campus Heredia
Curso programacion III
Autor: Darren De La O Gonzalez
Asunto:
"""

from ast import While
import os
os.system('cls')


# declarando variables trabajo

num = 0
aux = 0
dec = 0
uni = 0
linea = ""

# entrada de datos por teclado 
print("Ingrese un numero de dos digitos:")
linea = input()

if len(linea) ==2:


    # procesamiento de datos 
    num = int(linea) #convirtiendo un valor numerico en caracter 

    dec = num // 10
    uni = num % 10
    aux= (uni*10 )+dec

    # Salida de datos procesados
    print ("El numero invertido es: ",aux)

else:
    print("lo sentimos pero no se puede invertir un numero con mas de dos digitos ")
   # fin del if 
   
# ejemplo del ciclo for
for x in[1,3,4]:
  print("El valor de x es: ",x)

for c in['Karla','Lidia','Ana Paula',"Joseph",'Darren']:
 print("El nombre es :"+c)   
#fin del for 

#  ejemplos del ciclo while
cantidad=0
x=2
n=input("indique la cantidad de veces a ejecutarseel programa: ")
while x<=n:
    os.system('cls')
    largo = float(input("ingrese la medida de la pieza: "))
    if largo >= 1.2 and largo<=1.3:
        cantidad +=1 # cantidad = a cantidad + 1
        x+=1 #x=x+1
#fin while
print("la cantidad de piezas aptas son")
print(cantidad)
# fin del programa 