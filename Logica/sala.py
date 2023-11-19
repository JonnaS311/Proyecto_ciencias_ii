class Sala:

    def __init__(self, id, numero, actividad):
        self.__id = id
        self.__numero = numero
        self.__actividad = actividad
        self.__db_ruido = 0

    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def actividad(self):
        return self.__actividad

    @property
    def db_ruido(self):
        return self.__db_ruido

    def set_db_ruido(self, db_ruido):
        self.__db_ruido = db_ruido