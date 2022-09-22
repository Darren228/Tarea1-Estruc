## programa de ejemplo de uso de datos 


import os

os.system("cls")
#tipo de datos set(conjuntos )
Queque= "pastelito","jamon","papa", "mango","quesito"

print(Queque,type(Queque))

#tipo de datos Listas
b=["2.36","elefante", 1010,True,"rojo"]
print(b)

l4= b[1:5:2]
print(l4)

#tipos de datos diccionario
datos_basicos = {
"nombres":"Hillary",
"apellidos":"Madrigal Castillo",
"numero":"119780562",
"lugar_nacimiento":"San Jose COsta Rica",
"Nacionalidad":"Costarricense",
"Estado civil":"soltera"
}
print("\nDetalle del diccionario")
print("------------------")
print("\nClaves del diccionario", datos_basicos.keys())
print("\nValores del diccionario",datos_basicos.values())
print("\nElementos del diccionario", datos_basicos.items())





# exponente
g=5**2
print(g)


# division
d=5/2
d1=5//2
print(d,d1)

# modulo
m=7%2
print(m)

# operaciones relacionales
# a=5 se asignando el valor 5 a la varaiable a 
# a==5 se esta comparando el valor de a si es igual a 5

r=5 == 3
print(r)

r=5!= 3
print(r)

# () tuplas
# [] listas 
# {} diccionarios 

