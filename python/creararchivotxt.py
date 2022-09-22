


import os 
os.system('cls')

Archivo = open('D/Python progra/archivo.excls', 'w')
placa= input("digite la placa del automovil: ")
marca= input("digite la marca: ")
modelo = input("digite el modelo del automovil: ")
tipo = input("Digite el tipo de placa")



 Archivo.write(" La placa del automovil es : "+ placa + os.linesep)
 Archivo.write("La marca del automovil es:" + marca+ os.linesep)
 Archivo.write("El modelo del automovil es:" + modelo+ os.linesep)
 Archivo.write("La marca del automovil es:" + marca+ os.linesep)
 Archivo.write("El tipo del automovil es:" + tipo+ os.linesep)
 Archivo.close()
 