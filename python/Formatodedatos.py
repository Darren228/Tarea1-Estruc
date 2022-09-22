"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
Ejemplo de cadena de caracteres 
"""


import datetime
import os 
os.system('cls')

# funcion tabla de cuadrados y cubos

def TabCuadCubos():
    print("Esta linea ejecuto en la funcion TabCuadCub  ")
    for x in range(1,11):
     print('{0:2d}  --  {1:3d}  --  {2:4d}'.format(x, x*x,x*x*x))
#fin de la funcion 

  





# programa principal
año = 2016
evento = "lecciones"
"""
para usar formatted string literals 
F o f y todo va entre parentesis, llaves o corchetes 
"""

print(f'El resultado del año {año}, con el evento {evento}')

# recuperar la fecha actual del computador 
Fechaoriginal = datetime.datetime.now()
print("La fecha completa es: ", Fechaoriginal)

# solo fecha
fecha = Fechaoriginal.date()
print("La fecha es: ", fecha)

# solo año
Año = fecha.strftime("%Y")
print("El a;o es : ", Año)

# ------------------------------------
VotosValidos = 42_575_645
VotosInvalidos = 43_132_495

Porcentaje = VotosValidos / (VotosValidos+VotosInvalidos)

# salida formateada
print("Diccionario de datos")
print('La cantidad{:-9} votos validos {:2.2%}'.format(VotosValidos, Porcentaje))

# ---------------------------------------------------------------------------------------
tabla = {'Juan': 4127, 'Karla': 4098, 'Darren': 7678}

print(tabla)
print 
print 
for nombre,telefono in tabla.items():
    print(f'{nombre:10}  ===> {telefono:10d} ')

# carga de la funcion TabCuadCubos()
TabCuadCubos()
print("Esta linea ejecuto en el programa principal ")