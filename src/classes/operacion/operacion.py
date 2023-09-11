from abc import ABC, abstractmethod


class Operacion(ABC):
    def __init__(self, id, cuenta, monto, fecha, hora):
        self.__id = id
        self.__cuenta = cuenta
        self.__monto = monto
        self.__fecha = fecha
        self.__hora = hora

    @abstractmethod
    def realizar_operacion():
        pass
