from tkinter import *
from tkinter import messagebox
import pickle
from tkinter.ttk import Treeview

from Alumnos import Alumnos

def confVentana(ventana):
    ventana.config(width="700", height="700")
    ventana.config(bg="#656565")
    ventana.config(bd=25)
    ventana.config(relief=RIDGE)
    ventana.config(cursor="hand2")

def confLabel(ventana):
    Titulo = Label(ventana, text="ALUMNOS DEL CENTRO:")
    Titulo.grid(row = 0, column = 0)
    Titulo.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

def confTabla(ventana):
    ficheroApertura = open("lista", "rb")
    alumnos = pickle.load(ficheroApertura)
    ficheroApertura.close()

    for x in alumnos:
        print(x.getnombre() +" " +x.getapellido()+" "+x.getedad())

    tabla = Treeview(ventana,columns = ('#0','#1'))
    tabla.grid(row=1, column=0)
    tabla.heading("#0", text="Nombre",  anchor = CENTER)
    tabla.heading("#1", text="Apellido",  anchor = CENTER)
    tabla.heading("#2", text="Edad", anchor = CENTER)

    for x in alumnos:
       tabla.insert('',0,text = x.getnombre(), values=(x.getapellido(), x.getedad()))

class VerAlumnos:

    def ventana2(self):
        global raiz
        raiz = Tk()
        raiz.title("Ver Alumnos")
        # Creo el frame, lo añado a la raiz, y le doy diseño
        global ventana2
        ventana2 = Frame()
        ventana2.pack()
        confVentana(ventana2)
        confLabel(ventana2)
        confTabla(ventana2)


