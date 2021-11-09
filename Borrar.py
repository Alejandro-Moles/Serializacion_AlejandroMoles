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
    Titulo = Label(ventana, text="LISTA DE ALUMNOS DEL CENTRO:")
    Titulo.grid(row = 0, column = 0)
    Titulo.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

    Mensaje = Label(ventana, text="Seleccione el nombre del alumno que quieres borrar :")
    Mensaje.grid(row=2, column=0)
    Mensaje.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje2 = Label(ventana, text="Pulse para borrar")
    Mensaje2.grid(row=4, column=0)
    Mensaje2.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje3 = Label(ventana, text="Pulse para salir")
    Mensaje3.grid(row=6, column=0)
    Mensaje3.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

def confEntry(ventana):
    global mi_Entry
    mi_Entry = Entry(ventana)
    mi_Entry.grid(row=3, column=0)
    mi_Entry.config(bg="#656565", font=("Segoe Script", 18))

def confTabla(ventana):
    ficheroApertura = open("lista", "rb")
    alumnos = pickle.load(ficheroApertura)
    ficheroApertura.close()

    tabla = Treeview(ventana,columns = ('#0','#1'))
    tabla.grid(row=1, column=0)
    tabla.heading("#0", text="Nombre",  anchor = CENTER)
    tabla.heading("#1", text="Apellido",  anchor = CENTER)
    tabla.heading("#2", text="Edad", anchor = CENTER)

    for x in alumnos:
       tabla.insert('',0,text = x.getnombre(), values=(x.getapellido(), x.getedad()))


def confBoton(ventana):
    def borrarAlumno():
        ficheroApertura = open("lista", "rb")
        alumnos1 = pickle.load(ficheroApertura)
        ficheroApertura.close()

        if mi_Entry.get() == "":
            messagebox.showwarning("Error, introduzca valores         ")
            mi_Entry.delete(0, "end")
            mi_Entry.focus_set()
        else:
            for x in alumnos1:
                if x.getnombre() == mi_Entry.get():
                    alumnos1.remove(x)
                    messagebox.showinfo("Alumno borrado     ")

            fichero_binario = open("lista", "wb")
            pickle.dump(alumnos1, fichero_binario)
            fichero_binario.close()
            del (fichero_binario)
            mi_Entry.delete(0, "end")
        confTabla(ventana)

    def salir():
        messagebox.showinfo("Saliendo de la aplicacion    ")
        raiz.destroy()
    # boton 1
    boton_añadir = Button(ventana,command=borrarAlumno,text="Borrar")
    boton_añadir.grid(row=5, column=0)
    boton_añadir.config(font=("Courier", 24))

    # boton 1
    boton_salir = Button(ventana, command=salir, text="Salir")
    boton_salir.grid(row=7, column=0)
    boton_salir.config(font=("Courier", 24))
class Borrar:

    def ventana3(self):
        global raiz
        raiz = Tk()
        raiz.title("Borrar Alumnos")
        # Creo el frame, lo añado a la raiz, y le doy diseño
        global ventana2
        ventana3 = Frame()
        ventana3.pack()
        confVentana(ventana3)
        confLabel(ventana3)
        confTabla(ventana3)
        confEntry(ventana3)
        confBoton(ventana3)

