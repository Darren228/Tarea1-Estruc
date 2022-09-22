"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
Reto de la semana
Hacer un programa en Python que permita capturar una cadena de caracteres que incluya numero, caracteres especiales y letras por teclado, donde se requiere saber la cantidad de cada vocal usada en la cadena de caracteres,
 la cantidad de cada numero usado, la cantidad de caracteres especiales y la cantidad de consonantes. Para resolver esto se debe crear una función para que resuelva cada cantidad de caracteres requeridas
  e indicadas anteriormente y permitiendo que el resultado final sea generar por otra función
  Fecha: 27/02/22

"""

import os
os.system('cls')


def CaracteresNL(cadena):
    digitos = 0
    mayusculas = 0
    minusculas = 0
    letras = 0
    for c in cadena:
        if c.isdigit():
            digitos += 1
        if c.islower():
            mayusculas += 1
        if c.isupper():
            minusculas += 1
        if c.isalpha():
            letras += 1
        else:
            pass
    return digitos, mayusculas, minusculas, letras


texto = input('Digite un la oracion desada: ')
resultado = CaracteresNL(texto)
print("\n")
vocal = []
total = 0

caracter = []
caracdif = 0
for iniciador in [",", ".", ":", ";", "(", ")", "?", "@", "#", "%", "*", " "]:
    caracter.append(texto.count(iniciador))
    caracdif += texto.count(iniciador)


for iniciador in ["a","A","E" "e","I" "i","O" "o","U", "u"]:
    vocal.append(texto.count(iniciador))
    total += texto.count(iniciador)

consonan = []
totl = 0
for iniciador in ["b", "B", "C", "c", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k","L","l","M","m" "N", "n", "Ñ", "ñ", "P", "p", "Q", "q", "R", "r", "S", "s", "t", "T", "v", "V", "W", "w", "X", "x", "y", "Y", "Z", "z"]:
    consonan.append(texto.count(iniciador))
    totl += texto.count(iniciador)
    resultadototal = 0



resultadototal = resultado[1]+resultado[2]+resultado[0]+caracdif
print("Total de consonantes:", totl)
print("Total de Vocales:", total)
print('cantidad de digitos: %i' % resultado[0])
print('cantidad de minusculas : %i' % resultado[1])
print('cantidad de mayusculas : %i' % resultado[2])
print('cantidad de letras caracteres especiales :', caracdif)
print('cantidad de letras totales :%i' % resultadototal)
