"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez
Ejemplo de funciones
"""
import datetime
# Funcion 1 => no recive datos y no retorna ningun resultado de donde fue invocado 
def bienvenidad():
    print("Bienvenidos al tema de las funciones con python...")
 # fin

#  funcion 1 =>  recibe datos y no retorna ningun resultado de donde fue invocado
def sumar(nu1,nu2):
    resul = nu1 + nu2
    print(f"La suma del numero {nu1} mas el numero {nu2}, da como resultado el numero {resul} ")


# Funcion 3 => no recibe datos, pero retorna un resultado 
def multoplica():
    val1 = 4
    val2 = 7
    return val1 * val2
# fin

# funcion 4 recibe daros y retorna un resultado 
def calcuedad(AnNaci):
    FechaOriginal = datetime.datetime
    fecha = datetime.date()
    AñoAct = fecha.strftime

    return AñoAct - AñoNaci




# programa principal
import os
os.system('cls')
 # llamada la funcion Bienvenida 

bienvenidad()
print("\n\n\n")

# Llama a este otr
sumar(23,10)

# llama la funcion a multiplicar 
resultado = multoplica()
print("El resultado devuelto de la funcion multiplicar es : ", resultado)

# calcular a;o
AñoNaci = int(input("Digite el a;o de nacimiento: "))
print("La edad de la persona es: ", calcuedad(AñoNaci))