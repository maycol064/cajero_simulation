from .operacion import Operacion


class Retiro(Operacion):
    def realizar_operacion(self):
        print("Realizando operacion desde Retiro")
        # TODO: Realizar movimiento en la BD
