class Arista:

    def __init__(self, id, id_material_uno, id_material_dos, distancia):
        self.__id = id
        self.__id_material_uno = id_material_uno
        self.__id_material_dos = id_material_dos
        self.__distancia = distancia

    @property
    def id(self):
        return self.__id

    @property
    def id_material_uno(self):
        return self.__id_material_uno

    @property
    def id_material_dos(self):
        return self.__id_material_dos

    @property
    def distancia(self):
        return self.__distancia
