"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
programa controla la poblacion de pinguinos 
"""
from email.utils import decode_rfc2231
import os 
os.system("cls")

class MisPinguinos:
    def __init__(self):
        self.ContadorPin = 0
        # fin metodo __init__

    def agregar(self,numero = 1):
        # metodo que suma pinguinos por defecto determina un pinguino
        self.ContadorPin = self.ContadorPin+numero


    def extraer(self, numero = 1):
        self.ContadorPin -= numero

    def SaberCantidadPinguinos(self):
        return self.ContadorPin

    def __delattr__(self):
        pass

# zona de la rutina principal de la clase

# definicion del objeto 

Objpin = MisPinguinos()
# agregar pinguinos
Objpin.agregar(5)
# saber la cantidad de pinguinos que existen
print("La cantidad de pinguinos es: ",Objpin.SaberCantidadPinguinos())

# muerte pinguino
Objpin.extraer(1)

print("La cantidad de pinguinos es: ",Objpin.SaberCantidadPinguinos())
