


class alumnos():
 #definiendo metodo de inicializacion 
    def _init_(self,nombre=""):
        self.nombre = nombre #stributo de tipo publico 
        
          #atributo encapsualdo
        self.__AtriSecreto = "asdfgh"



# definiendo objeto

a1 = alumnos("julio")
a2 = alumnos()

print(a1.nombre)


a2.__AtriSecreto
print(a2.__AtriSecreto)





