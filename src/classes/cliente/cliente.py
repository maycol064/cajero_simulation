class Cliente():
    def __init__(self, id, nombre, apellido_paterno, apellido_materno):
        self.__id = id
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno

    def get_informacion(self):
        print(self.__str__())

    def __str__(self):
        return f"Cliente: {self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}\n"
