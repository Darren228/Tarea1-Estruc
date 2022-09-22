'''
representacion de un punto en el plano cartesiano, los atributos son x e y que presenta
los valores de las coordenadas cartesianas
'''
import math
import os 

class punto():
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    # fin del metodo inicial __init__

    def mostrar(self):
        return str(self.x)+":"+str(self.y)
    # fin del metodo mostrar

    def distancia(self, otro):
        # devuelve la distancia entre el punto a con el punto b 
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx*dx + dy*dy))

# main 
os.system('cls')

# creacion de objetos y constructores
punto1 = punto() #Este es un constructor de vacio 
punto2 = punto(4,5) #estre es un constructor con valores 
                       
print(punto1.distancia(punto2))
print()
print("el valor de punto2,x es: ", punto2.x)
punto2.x = 7
print("el valor de punto2,x es: ", punto2.x)

#fin de la clase

