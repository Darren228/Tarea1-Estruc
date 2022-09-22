import tkinter as tk
from tkinter import ttk
from tkinter import ttk

Vent = tk.Tk()
Vent.geometry('300x200')
Vent.resizable(False,False)
Vent.title('demostracion de la aplicacion de botones')



tk.Label(Vent,text='Esta es una etiqueta clasica' ).pack()
ttk.Label(Vent, text='Etiqueta tipo tema').pack()

exit_button = ttk.Button(
    Vent,
    text= 'salir'
    command=lambda: Vent.quit()
)

# presentar el boton en la pantalla
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True

)

Vent.mainloop()

