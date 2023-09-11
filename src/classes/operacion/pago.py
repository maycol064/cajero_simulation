from .operacion import Operacion


class Pago(Operacion):
    def __init__(self, id, cuenta, monto, fecha, hora, destino, forma_pago):
        # Cuenta funciona como cuenta origen
        super().__init__(id, cuenta, monto, fecha, hora)
        self.__destino = destino
        self.__forma_pago = forma_pago

    def realizar_operacion(self):
        print("Realizando operacion desde Pago...\n")
        # TODO: Realizar movimiento en la BD
