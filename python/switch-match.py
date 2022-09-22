# programa usa comando mathc para manejar las opciones de un switch 

import os
os.system('cls')

def DiasSemana(dia):
    match dia: 
        case 1: 
            return "lunes"
        case 2:
            return "martes"
        case 3:
            return "miercoles"
        case 4: 
            return "jueves"
        case 5:
            return "viernes"
        case 6:
            return "sabado"
        case 7: 
            return "domingo"
        case _: #opcion que oresenta en el caso de no coincidir cin ninguna de las opciones 
             return "por favor ingrese un numero de dia valido..."


print(DiasSemana(5))
print(DiasSemana(2))
print(DiasSemana(7))
print(DiasSemana(30))
