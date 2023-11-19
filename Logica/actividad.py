class Actividad:

    def __init__(self, nombre, max_db):
        self.__nombre = nombre
        self.__max_db = max_db

    @property
    def nombre(self):
        return self.__nombre

    @property
    def max_db(self):
        return self.__max_db
