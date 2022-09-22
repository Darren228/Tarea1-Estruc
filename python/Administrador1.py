#Programa para la administracion de partes
from tkinter import *
from tkinter import messagebox
from dbSQLite import Database
import os
os.system('cls')

db = Database ('Soda.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)
#fin funcion populate_list 

def add_item():
    if part_text.get() == '' or cliente_text.get() =='' or deta_text.get() == '' or precio_text.get() =='':
        messagebox.showerror('Campos Requeridos', 'por favor de rellenar todos los campos de la pantalla')
        return
    db.insert(part_text.get(), cliente_text.get(), deta_text.get(), precio_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get(), cliente_text.get, deta_text.get(), precio_text.get()))
    clear_text()
    populate_list()
#fin funcion add_item

def select_item(event):
    try:
        global select_item
        index = parts_list.curselection()[0]
        select_item= parts_list.get(index)
        print(select_item)

        #Seccion de asignacion de los datos leidos a cada textbox
        part_entry.delete(0,END)
        part_entry.insert(END,select_item[1])
        cliente_entry.delete(0, END)
        cliente_entry.insert(END, select_item[2])
        deta_entry.delete(0,END)
        deta_entry.insert(END, select_item[3])
        precio_entry.delete(0,END)
        precio_entry.insert(END, select_item[4])

    except IndexError:
        pass
#fin funcion select_item

def remove_item():
    db.remove(select_item[0])
    clear_text()
    populate_list()
#fin de la funcion remove_item

def update_item():
    db.update(select_item[0], part_text.get(), cliente_text.get(), deta_text.get(),precio_text.get())
    clear_text()
    populate_list()
#fin de la funcion clear_text

def clear_text():
    part_entry.delete(0,END)
    cliente_entry.delete(0,END)
    deta_entry.delete(0,END)
    precio_entry.delete(0,END)
#fin de la funcion clear_text

#Seccion de la creacion de la interfaz grafiacas de control de partes de una tienda 
app = Tk()

#Seccion de los datos de las partes 
part_text = StringVar()
part_label = Label(app,text ='Nombre de la parte', font=('bold',14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)

#Seccion de los datos del cliente 
cliente_text = StringVar()
cliente_label= Label(app,text='cliente',font=('bold',14),pady=20)
cliente_label.grid(row=0, column=0,sticky=W)
cliente_entry=Entry(app, textvariable=cliente_text)
cliente_entry.grid(row=0,column=3)

#Seccion de los datos del Detallista
deta_text = StringVar()
deta_label= Label(app,text='detallista',font=('bold',14),pady=20)
deta_label.grid(row=0, column=0,sticky=W)
deta_entry=Entry(app, textvariable=cliente_text)
deta_entry.grid(row=1,column=1)

#Seccion de los datos del Precio
precio_text = StringVar()
precio_label= Label(app,text='detallista',font=('bold',14),pady=20)
precio_label.grid(row=0, column=0,sticky=W)
precio_entry=Entry(app, textvariable=cliente_text)
precio_entry.grid(row=1,column=3)

#listado de partes (listbox)
parts_list = Listbox(app,height=8,width=50, border=0)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

#creando la barra del scroll
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,column=3)

#configurar el movimiento del scroll con el listbox
parts_list.configure(yscrollcommand=Scrollbar.set)
scrollbar.configure(command=parts_list.yview)
parts_list.blind('<<ListboxSelect>>', select_item)

#seccion de botones

#Boton agregar
add_btn=Button(app, text='Agregar una parte', width=15,command=add_item)
add_btn.grid(row=2,column=0,pady=20)

#boton de eliminar
remove_btn=Button(app, text='eliminar una parte', width=15,command=add_item)
remove_btn.grid(row=2,column=1)

#Boton de actualizar una parte
update_btn=Button(app, text='Actualizar una parte', width=15,command=add_item)
update_btn.grid(row=2,column=2)

#boton para limpiar
clear_btn=Button(app, text='Agregar una btn.gridparte', width=15,command=add_item)
clear_btn.grid(row=2,column=3)

#comando para poner el titulo a la ventana 
app.title('Administrador de partes')

#comando para dimensionar la ventena 
app.geometry('550x350')

#carga de datos listbox
populate_list()

#Inicio del programa 
app.mainloop()

