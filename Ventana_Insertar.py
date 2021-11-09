
from tkinter import *
from tkinter import messagebox
import pickle
from Alumnos import Alumnos


def confVentana(ventana):
    ventana.config(width="500", height="500")
    ventana.config(bg="#656565")
    ventana.config(bd=25)
    ventana.config(relief=RIDGE)
    ventana.config(cursor="hand2")

def confLabel(ventana):
    Titulo = Label(ventana, text="ALUMNOS DEL CENTRO:")
    Titulo.place(x=0, y=0)
    Titulo.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

    Nombre = Label(ventana, text="Nombre:")
    Nombre.place(x=10, y=80)
    Nombre.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

    Apellido = Label(ventana, text="Apellido:")
    Apellido.place(x=10, y=160)
    Apellido.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

    Edad = Label(ventana, text="Edad:")
    Edad.place(x=10, y=240)
    Edad.config(bg="#656565", font=("Segoe Script", 23), fg="#1c296d")

def confEntry(ventana):
    global text_Nombre
    text_Nombre = Entry()
    text_Nombre.place(x=200, y=120)
    text_Nombre.config(bg="#656565", font=("Arial", 18), fg="#000000")

    global text_Apellido
    text_Apellido = Entry()
    text_Apellido.place(x=200, y=200)
    text_Apellido.config(bg="#656565", font=("Arial", 18), fg="#000000")

    global text_Edad
    text_Edad = Entry()
    text_Edad.place(x=200, y=280)
    text_Edad.config(bg="#656565", font=("Arial", 18), fg="#000000")

def iniciarbotones(ventana, raiz):
    global lista
    lista = []
    def insertar():
        for datos in lista:
            print(datos.getnombre() +" " +datos.getapellido()+" "+datos.getedad())

        fichero_binario = open("lista", "wb")
        pickle.dump(lista, fichero_binario)
        fichero_binario.close()
        del(fichero_binario)

        messagebox.showinfo("Alumnos fichados     ")
        raiz.destroy()


    def añadirAlumnos():
        if text_Nombre.get() == "" or text_Apellido.get() == "" or text_Edad.get() == "" :
            messagebox.showwarning("Error, introduzca valores         ")
        else:
            alumno = Alumnos(text_Nombre.get(), text_Apellido.get(), text_Edad.get())
            lista.append(alumno)
            text_Nombre.delete(0, "end")
            text_Apellido.delete(0, "end")
            text_Edad.delete(0, "end")
            text_Nombre.focus_set()
            messagebox.showinfo("Alumnos introducido a clase      ")



    # boton 1
    boton_añadir = Button(ventana,command=añadirAlumnos ,text="Añadir")
    boton_añadir.place(x=30, y=350)
    boton_añadir.config(font=("Courier", 24))

    # boton 2
    boton_insertar = Button(ventana, command=insertar, text="Insertar")
    boton_insertar.place(x=230, y=350)
    boton_insertar.config(font=("Courier", 24))

class Insertar:

    def ventana1(self):
        global raiz
        raiz = Tk()
        raiz.title("Insertar Alumno")
        # Creo el frame, lo añado a la raiz, y le doy diseño
        global ventana1
        ventana1 = Frame()
        ventana1.pack()
        confVentana(ventana1)
        confLabel(ventana1)
        confEntry(ventana1)
        iniciarbotones(ventana1, raiz)

