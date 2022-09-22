"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
Ejemplo de cadena de caracteres 
"""

import os
os.system('cls')

# comillas simples 
cadena1 = 'texto entre comillas simples.'
print(cadena1, type(cadena1))

cadena2 = "texto  entre comillas"
print(cadena2, type(cadena2))

cadenas = cadena1 + cadena2

print(cadenas)

print("La cantidad de caracteres de la cadena es: ",len(cadenas))

