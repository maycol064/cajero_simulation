from random import randint
from time import sleep
import mysql.connector

# Datos BD
host = ""
user = ""
password = ""
database = ""

connection = mysql.connector.connect(
    host,
    user,
    password,
    database
);

CLAVE = 1234


def hacer_deposito(cantidad, saldo):
    return saldo + cantidad


def pago_servicio():
    servicio = input('Ingrese el nombre del servicio: ')
    referencia = input('Ingrese la referencia del servicio: ')
    monto = int(input('Ingrese el monto a pagar: '))
    metodo = int(input(
        'Seleccione el método de pago: \n1. Efectivo\n2. Saldo en la cuenta\n3. Tarjeta de crédito\n'))
    if metodo == 1:
        input('Ingrese los billetes... (presione cualquier tecla para continuar)')
        sleep(3)
        print(
            f'Monto completo...\nPago a {servicio} con referencia {referencia} realizado.\nUsted ha pagado la cantidad ${monto} con efectivo')
        return [1, 0]
    elif metodo == 2:
        print('Realizando pago...')
        sleep(3)
        print(
            f'Monto completo...\nPago a {servicio} con referencia {referencia} realizado.\nUsted ha pagado la cantidad ${monto} con el saldo de su cuenta')
        return [2, monto]
    elif metodo == 3:
        print('Realizando pago...')
        sleep(3)
        print(
            f'Monto completo...\nPago a {servicio} con referencia {referencia} realizado.\nUsted ha pagado la cantidad ${monto} con tarjeta de crédito')
        return [3, monto]

    servicio = input('Ingrese el nombre del servicio')
    referencia = input('Ingrese la referencia del servicio')
    monto = int(input('Ingrese el monto a pagar'))
    metodo = int(input(
        'Seleccione el método de pago: \n1. Efectivo\n2. Saldo en la cuenta\n3. Tarjeta de crédito'))
    if metodo == 1:
        input('Ingrese los billetes... (presione cualquier tecla para continuar)')
        sleep(5)
        print(
            f'Monto completo...\nPago a {servicio} con referencia {referencia} realizado.\nUsted ha pagado la cantidad ${monto} con efectivo')
        return [1, 0]
    elif metodo == 2:
        print('Realizando pago...')
        sleep(5)
        print(
            f'Monto completo...\nPago a {servicio} con referencia {referencia} realizado.\nUsted ha pagado la cantidad ${monto} con el saldo de su cuenta')
        return [2, monto]
    elif metodo == 3:
        print('Realizando pago...')
        sleep(5)
        print(
            f'Monto completo...\nPago a {servicio} con referencia {referencia} realizado.\nUsted ha pagado la cantidad ${monto} con tarjeta de crédito')
        return [3, monto]


def transferencia():
    destino = int(input('Ingrese la cuenta destino de la transferencia: '))
    banco = input('Ingrese el banco: ')
    beneficiario = input('Ingrese el nombre del beneficiario: ')
    monto = int(input('Ingrese el monto: '))
    print(f'Usted a transferido ${monto} a {beneficiario} con cuenta: {destino} del banco {banco}')
    return monto


def retiro():
    monto = int(input('Ingrese el monto a retirar: '))
    print(f'Ha retirado de su cuenta ${monto}\n')
    return monto


def main():
    saldo = randint(1000, 200000)
    credito = 50000
    while True:
        print('Bienvenido a tu cuenta')
        nip = int(input("\nIngresa tu clave: "))

        if nip == CLAVE:
            # Menu
            eleccion = ''
            while eleccion != '6':
                eleccion = input(
                    '\nSeleccione opción: \n1. Consultar saldo.\n2. Transacciones \n')
                if eleccion == '1':
                    print(
                        f'\nConsulta saldo\nTu saldo en débito es es: {saldo}\nTu crédito disponible es: {credito}\n\n')
                elif eleccion == '2':
                    eleccion_transacciones = ''
                    while eleccion_transacciones != 'a' or eleccion_transacciones != 'b' or eleccion_transacciones != 'c' or eleccion_transacciones != 'd' or eleccion_transacciones != 'e':
                        eleccion_transacciones = input(
                            '\nSeleccione una opción: \na. Depósito\nb. Pago servicio\nc. Pago impuestos\nd. Transferencias \ne. Retiro\n')
                        if eleccion_transacciones == 'a':
                            cantidad = int(input('\nIngrese el monto: '))
                            total = hacer_deposito(cantidad, saldo)
                            saldo = total
                            print(f'Saldo actualizado: {total}')
                            break
                        if eleccion_transacciones == 'b':
                            [opc, monto] = pago_servicio()
                            if opc == 1:
                                break
                            elif opc == 2:
                                saldo = saldo - monto
                                break
                            elif opc == 3:
                                credito = credito - monto
                                break
                        if eleccion_transacciones == 'c':
                            [opc, monto] = pago_servicio()
                            if opc == 1:
                                break
                            elif opc == 2:
                                saldo = saldo - monto
                                break
                            elif opc == 3:
                                credito = credito - monto
                                break
                        if eleccion_transacciones == 'd':
                            total = transferencia()
                            saldo = saldo - total
                            break
                        if eleccion_transacciones == 'e':
                            total = retiro()
                            saldo = saldo - total
                            break
                elif eleccion == '3':
                    while True:
                        clave = int(input('\nIngresa tu nueva clave'))
                        if len(clave == 4):
                            break
        else:
            print('Clave INCORRECTA\n\n')

if __name__ == '__main__':
    main()
