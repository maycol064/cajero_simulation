from random import randint

class bank_client:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.saldo = randint(1000, 300000)

    def mostrar_informacion(self):
        print(f"name: {self.name}")
        print(f"last_name: {self.last_name}")
        print(f"Saldo: ${self.saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("No tienes suficiente saldo para realizar esta operación o la cantidad es inválida.")

# Crear un objeto de la clase Usuario
usuario1 = usuario("Juan Pérez", "juan@example.com")

# Mostrar información del usuario
usuario1.mostrar_informacion()

# Realizar depósitos y retiros
usuario1.depositar(100)
usuario1.retirar(50)

# Mostrar información actualizada
usuario1.mostrar_informacion()
