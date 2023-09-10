class Cuenta:
    def __init__(self, id, tipo_cuenta, cliente, nip, saldo):
        self.__id = id
        self.__tipo_cuenta = tipo_cuenta
        self.__cliente = cliente
        self.__nip = nip
        self.__saldo = saldo

    def validar_cuenta(self, nip_ingresado):
        return nip_ingresado == self.__nip

    def tiene_saldo_disponible(self, monto_operacion):
        return self.__saldo >= monto_operacion

    def ingresar_tarjeta(self, id):
        print("Ingresando tarjeta...\n")
        # TODO: Validar si existe la cuenta en la BD
