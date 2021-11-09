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
    ventana.grid(column = 0, row=0, pady=(10,10))

def confLabel(ventana):
    Titulo = Label(ventana, text="LISTA DE ALUMNOS DEL CENTRO:")
    Titulo.grid(row = 0, column = 0, columnspan=3)
    Titulo.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

    Mensaje = Label(ventana, text="nombre del alumn a modificar :")
    Mensaje.grid(row=2, column=0)
    Mensaje.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje2 = Label(ventana, text="apellido alumno a modificar :")
    Mensaje2.grid(row=2, column=1)
    Mensaje2.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje3 = Label(ventana, text="Nombre")
    Mensaje3.grid(row=4, column=0)
    Mensaje3.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje4 = Label(ventana, text="Apellido")
    Mensaje4.grid(row=4, column=1)
    Mensaje4.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje5 = Label(ventana, text="Edad")
    Mensaje5.grid(row=4, column=2)
    Mensaje5.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")


    Mensaje6 = Label(ventana, text="Pulse para modificar")
    Mensaje6.grid(row=6, column=0)
    Mensaje6.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

    Mensaje7 = Label(ventana, text="Pulse para salir")
    Mensaje7.grid(row=6, column=1)
    Mensaje7.config(bg="#656565", font=("Segoe Script", 18), fg="#1c296d")

def confEntry(ventana):
    global mi_Entry
    mi_Entry = Entry(ventana)
    mi_Entry.grid(row=3, column=0)
    mi_Entry.config(bg="#656565", font=("Segoe Script", 18))

    global mi_Entry2
    mi_Entry2 = Entry(ventana)
    mi_Entry2.grid(row=3, column=1)
    mi_Entry2.config(bg="#656565", font=("Segoe Script", 18))

    global Nombre
    Nombre = Entry(ventana)
    Nombre.grid(row=5, column=0)
    Nombre.config(bg="#656565", font=("Segoe Script", 18))

    global Apellido
    Apellido = Entry(ventana)
    Apellido.grid(row=5, column=1)
    Apellido.config(bg="#656565", font=("Segoe Script", 18))

    global Edad
    Edad = Entry(ventana)
    Edad.grid(row=5, column=2)
    Edad.config(bg="#656565", font=("Segoe Script", 18))

def confTabla(ventana):
    ficheroApertura = open("lista", "rb")
    alumnos = pickle.load(ficheroApertura)
    ficheroApertura.close()

    tabla = Treeview(ventana,columns = ('#0','#1'))
    tabla.grid(row=1, column=0, columnspan=3)
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

        if mi_Entry.get() == "" or mi_Entry2.get() == "":
            messagebox.showwarning("Error, introduzca valores         ")
            mi_Entry.delete(0, "end")
            mi_Entry.focus_set()
        else:
            for x in alumnos1:
                if x.getnombre() == mi_Entry.get() and x.getapellido() == mi_Entry2.get():
                    x.setnombre(Nombre.get())
                    x.setapellido(Apellido.get())
                    x.setedad(Edad.get())
                    messagebox.showinfo("Alumno modificado     ")

            fichero_binario = open("lista", "wb")
            pickle.dump(alumnos1, fichero_binario)
            fichero_binario.close()
            del (fichero_binario)
            mi_Entry.delete(0, "end")
            mi_Entry2.delete(0, "end")
            Nombre.delete(0, "end")
            Apellido.delete(0, "end")
            Edad.delete(0, "end")
        confTabla(ventana)

    def salir():
        messagebox.showinfo("Saliendo de la aplicacion    ")
        raiz.destroy()
    # boton 1
    boton_modificar = Button(ventana,command=borrarAlumno,text="Modificar")
    boton_modificar.grid(row=7, column=0)
    boton_modificar.config(font=("Courier", 24))

    # boton 1
    boton_salir = Button(ventana, command=salir, text="Salir")
    boton_salir.grid(row=7, column=1)
    boton_salir.config(font=("Courier", 24))
class Modificar:

    def ventana4(self):
        global raiz
        raiz = Tk()
        raiz.title("Modificar Alumnos")
        # Creo el frame, lo añado a la raiz, y le doy diseño
        global ventana2
        ventana4 = Frame()
        ventana4.pack()
        confVentana(ventana4)
        confLabel(ventana4)
        confTabla(ventana4)
        confEntry(ventana4)
        confBoton(ventana4)

