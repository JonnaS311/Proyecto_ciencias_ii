class Material:
    def __init__(self, id, nombre, resistencias_frecuencias):
        self.__id = id
        self.__nombre = nombre
        self.__resistencias_frecuencias = resistencias_frecuencias

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def resistencias_frecuencias(self):
        return self.__resistencias_frecuencias
