from tkinter import *

comedor = Tk()
comedor.title("Venta de Comida")
comedor.geometry("1285x630+0+0")
comedor.config(bg="white")
encabezado = Label(comedor, text="Servicio de Comida", bd=10,relief=GROOVE,
font=("Arial Black", 20),bg="#000099", fg="white").pack(fill=X)

detalles = LabelFrame(comedor, text="Servicios que ofrecemos",font=("Arial Black", 14),
    bg="#000099", fg="white",bd=10,relief=GROOVE)
detalles.place(x=0, y=80, height=410, relwidth=1) 

arroz = Label(detalles, text="Arroz blanco",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=0, column=0,padx=8, pady=11)
entry1 = Entry(detalles,font=("arial", 7, "bold"), borderwidth=4,width=20).grid(row=0,column=1,padx=8)

arroz_amarillo = Label(detalles, text="Arroz amarillo",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=1, column=0,padx=8, pady=11)
entry2 = Entry(detalles,font=("arial", 7, "bold"), borderwidth=4,width=20).grid(row=1,column=1,padx=8)

moro = Label(detalles, text="Moro de Guandulez",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=2, column=0,padx=8, pady=11)
entry3 = Entry(detalles,font=("arial", 7, "bold"), borderwidth=4,width=20).grid(row=2,column=1,padx=8)

moro2 = Label(detalles, text="Moro de habichuelas",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=3, column=0,padx=8, pady=11)
entry4 = Entry(detalles,font=("arial", 7, "bold"), borderwidth=4,width=20).grid(row=3,column=1,padx=8)

cosido = Label(detalles, text="Cosido con Arroz",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=4, column=0,padx=8, pady=11)
entry5 = Entry(detalles,font=("arial", 7, "bold"), borderwidth=4,width=20).grid(row=4,column=1,padx=8)

pollo = Label(detalles, text="Carne de pollo",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=0, column=2,padx=8, pady=11)
entry5 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=0,column=3,padx=8)

vaca = Label(detalles, text="Carne de vaca",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=1, column=2,padx=8, pady=11)
entry6 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=1,column=3,padx=8)

cerdo = Label(detalles, text="Carne de cerdo",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=2, column=2,padx=8, pady=11)
entry7 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=2,column=3,padx=8)

chivo = Label(detalles, text="Carne de chivo",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=3, column=2,padx=8, pady=11)
entry8 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=3,column=3,padx=8)

chuleta = Label(detalles, text="Chuleta",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=4, column=2,padx=8, pady=11)
entry9 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=4,column=3,padx=8)

jugo_natural = Label(detalles, text="Jugos naturales",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=0, column=4,padx=8, pady=11)
entry10 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=0,column=5,padx=8)

piña = Label(detalles, text="Piña con leche",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=1, column=4,padx=8, pady=11)
entry11 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=1,column=5,padx=8)

chinola = Label(detalles, text="Chinola con avena",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=2, column=4,padx=8, pady=11)
entry12 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=2,column=5,padx=8)

refrescos = Label(detalles, text="Refrescos",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=3, column=4,padx=8, pady=11)
entry13 = Entry(detalles,font=("arial", 7, "bold") ,borderwidth=4,width=20).grid(row=3,column=5,padx=8)

limon = Label(detalles, text="Limon con avena",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=4, column=4,padx=8, pady=11)
entry14 = Entry(detalles, font=("arial", 7, "bold"), borderwidth=4,width=20).grid(row=4,column=5,padx=8)

calculadora = Frame(detalles, bd=10, relief=GROOVE, bg="#000099")
calculadora.place(x=950, y=0, width=300, height=700)

textDisplay = Entry(calculadora,font=("arial", 18, "bold"),bd=10,insertwidth=4, bg="white",justify="left")
textDisplay.grid(columnspan=4)

btn7=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="7", bg="white").grid(row=2,column=0)

btn8=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="8", bg="white").grid(row=2,column=1)

btn9=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="9", bg="white").grid(row=2,column=2)

Addition=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="+", bg="white").grid(row=2,column=3)

btn4=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="4", bg="white").grid(row=3,column=0) 

btn5=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="5", bg="white").grid(row=3,column=1)

btn6=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="6", bg="white").grid(row=3,column=2)

subtraccion=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial",15 , "bold"), text="-", bg="white").grid(row=3,column=3)

btn1=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="1", bg="white").grid(row=4,column=0) 

btn2=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="2", bg="white").grid(row=4,column=1)

btn3=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="3", bg="white").grid(row=4,column=2)

multiply=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="*", bg="white").grid(row=4,column=3)

btn0=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="0", bg="white").grid(row=5,column=0) 

btnClear=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="C", bg="white").grid(row=5,column=1)

btnEquals=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="=", bg="white").grid(row=5,column=2)

Division=Button(calculadora,padx=16,pady=16,bd=5, fg="black", font=("arial", 15, "bold"), text="/", bg="white").grid(row=5,column=3)

resumen = LabelFrame(comedor, text="Total de la Compra",font=("Arial black", 14),relief=GROOVE,
    bd=5,bg="#000099",fg="white")
resumen.place(x=0, y=490, relwidth=1, height=140) 


total_arroz = Label(resumen, text="Precio Total Arroz",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=0, column=0)
entry_arroz = Entry(resumen,borderwidth=2,width=30).grid(row=0,column=1,padx=10,pady=7)


total_carne = Label(resumen, text="Precio Total Carne",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=1, column=0)
entry_carne = Entry(resumen,borderwidth=2,width=30).grid(row=1,column=1,padx=10,pady=7)

total_jugos = Label(resumen, text="Precio Total Jugos",font=("Arial black", 12),bg="#000099",
fg="white").grid(row=2, column=0)
entry_jugos = Entry(resumen,borderwidth=2,width=30).grid(row=2,column=1,padx=10,pady=7)

boton_frame = Frame(resumen, bd=7,relief=FLAT,bg="#000099")
boton_frame.place(x=500, width=700, height=95)

boton_total = Button(boton_frame, text="Total", width=15,font=("Arial black", 12),
pady=10,bg="#000099",fg="white").grid(row=0,column=0,padx=12,pady=10)

boton_Limpiar = Button(boton_frame, text="Reiniciar", width=15,font=("Arial black", 12),
pady=10,bg="#000099",fg="white").grid(row=0,column=1,padx=12,pady=10)

boton_salir = Button(boton_frame, text="Salir", width=15,font=("Arial black", 12),
pady=10,bg="#000099",fg="white").grid(row=0,column=2,padx=12,pady=10)










comedor.mainloop()