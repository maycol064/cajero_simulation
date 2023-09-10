from ..operacion import Operacion

# El movimiento puede ser una transferencia o depósito


class Movimiento(Operacion):
    def __init__(self, id, cuenta, fecha, hora, destino):
        super().__init__(id, cuenta, fecha, hora)
        self.__destino = destino

    def realizar_operacion():
        print("Realizando operacion desde Movimiento")
        # TODO: Realizar movimiento en la BD
