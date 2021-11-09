from tkinter import *
from Ventana_Insertar import *
from VerAlumnos import *
from Borrar import *
from Modificar import *



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


def iniciarbotones(ventana, raiz):
    def cerrarventana():
        raiz.destroy()
        v1 = Insertar()
        v1.ventana1()

    def veralumnos():
        raiz.destroy()
        v2 = VerAlumnos()
        v2.ventana2()

    def borraralumnos():
        raiz.destroy()
        v3 = Borrar()
        v3.ventana3()

    def modificar():
        raiz.destroy()
        v4 = Modificar()
        v4.ventana4()
    # boton 1
    boton_insertar = Button(ventana,command = cerrarventana, text="Insertar")
    boton_insertar.place(x=130, y=70)
    boton_insertar.config(font=("Courier", 24))

    # boton 2
    boton_listar = Button(ventana,command = veralumnos, text="Ver")
    boton_listar.place(x=130, y=150)
    boton_listar.config(font=("Courier", 24))

    # boton 3
    boton_borrar = Button(ventana,command= borraralumnos, text="Borrar")
    boton_borrar.place(x=130, y=250)
    boton_borrar.config(font=("Courier", 24))

    # boton 4
    boton_modificar = Button(ventana,command=modificar, text="Modificar")
    boton_modificar.place(x=130, y=350)
    boton_modificar.config(font=("Courier", 24))

class Vista:
    raiz =Tk()
    raiz.title("Serializacion Python")
    #Creo el frame, lo añado a la raiz, y le doy diseño
    ventana = Frame()
    ventana.pack()

    confVentana(ventana)
    confLabel(ventana)
    iniciarbotones(ventana, raiz)

    raiz.mainloop()



