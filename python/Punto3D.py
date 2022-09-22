


from tkinter import Y
from punto import punto

# definiendo la calse local
class punto3d(punto): 
    def __init__(self, x=0, y=0,z=0):
        super().__init__(x, y)
        self.z=z
    # fin del metodo __intit__

    @property
    def z(self):
        print("DOy z")
        return self.__z

    # fin metodo

    @z.setter
    def z(self,z):
        print("Cambio z")
        self.__z=z
        # fin del metodo

    def mostrar(self):
            return super().mostrar()+":"+str(self.__z)
    def distancia(self, otro):
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy + dz*dz)**0.5
    # fin del metodo

import os
os.system('cls')

# main
p3d = punto3d(1,2,3)
print(p3d.x)
print(p3d.z)

p3d.mostrar()
p3d.y = 3
print(p3d.y)

# fin de la clase

