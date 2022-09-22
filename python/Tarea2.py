"""Universidad politecnica internaciona
autor:Darren De La O Gonzalez. Steven Barquero, Sebastian Esquivel
trabajo extra clase Tkinter
"""



import tkinter 

import os
os.system('cls')

ventana = tkinter.Tk()
ventana.geometry("300x300")

cajaTexto=tkinter.Entry(ventana)
cajaTexto.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack() 


def textoDeLaCaja():
    text200 = cajaTexto.get()
    etiqueta["text"]= text200

    text200 = cajaTexto.get()
    etiqueta["text"]= text200

cajaTexto2=tkinter.Entry(ventana)
cajaTexto2.pack()

etiqueta2 = tkinter.Label(ventana)
etiqueta2.pack() 

def textoDeLaCaja2():
    MontoAumento =0
    PorAu = "No definido"
    Numero200 = cajaTexto2.get()
    etiqueta2["text"]=Numero200
    if cajaTexto2 < 10000:
        PorAu = "25%" #PorAu => porcentaje de aumento
        MontoAumento=(cajaTexto2 * 25)/100 # MontoAumento => contiene el monto a ser aumentado en salario del 

    if cajaTexto2 >=11000 and cajaTexto2 < 20000:
        PorAu = "10%"
        MontoAumento=(cajaTexto2 * 10)/100
    if cajaTexto2 >=20000 and cajaTexto2 < 50000:
        PorAu = "5%"
        MontoAumento=(cajaTexto2 * 5)/100
    if 50000 <= cajaTexto2  < 90000:
        print("Lo sentimos mucho, pero no tiene aumento.....")

boton1 =tkinter.Button(ventana,text = "ingrese el nombre del empleado", command= textoDeLaCaja)
boton1.pack()

boton2 =tkinter.Button(ventana,text = "ingrese el salario del empleado", command= textoDeLaCaja2)
boton2.pack()

ventana.mainloop()




