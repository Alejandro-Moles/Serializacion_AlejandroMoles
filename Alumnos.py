class Alumnos:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    def getnombre(self):
        return self.__nombre

    def getapellido(self):
        return self.__apellido

    def getedad(self):
        return self.__edad

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setapellido(self, apellido):
        self.__apellido = apellido

    def setedad(self, edad):
        self.__edad = edad