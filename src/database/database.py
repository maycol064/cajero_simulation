import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Carga la configuración desde el .env. Necesitan instalar dotenv:)
# pip install python-dotenv
# pip install mysql-connector.python


class Database():
    def __init__(self):
        self.__conection_values = dotenv_values()
        self.__configuration = {
            'user': self.__conection_values['DB_USER'],
            'password': self.__conection_values['DB_PASSWORD'],
            'host': self.__conection_values['DB_HOST'],
            'database': self.__conection_values['DB_DATABASE'],
        }

    def select(self, query, data_query=None):
        cnx = mysql.connector.connect(**self.__configuration)
        cursor = cnx.cursor()

        if data_query == None:
            cursor.execute(query)
        else:
            cursor.execute(query, data_query)

        result = []
        for data_result in cursor:
            result.append(data_result)

        cursor.close()
        cnx.close()

        return result

    def insert_or_update(self, query, data_query):
        cnx = mysql.connector.connect(**self.__configuration)
        cursor = cnx.cursor()

        cursor.execute(query, data_query)
        cnx.commit()

        cursor.close()
        cnx.close()


database = Database()

# devuelve una lista vacía
print(database.select("SELECT * FROM banco WHERE nombre = %s", ('Santaner',)))


# Devuelve todos los bancos
print(database.select("SELECT * FROM banco"))

# Inserta un nuevo banco
database.insert_or_update(
    "INSERT INTO banco VALUES(%s, %s)", ("31", "Banco del Bienestar")
)
print(database.select("SELECT * FROM banco"))

# Actualizar un banco
database.insert_or_update(
    "UPDATE banco SET nombre = %s WHERE id_banco = %s", ("Bienestar", "31")
)
print(database.select("SELECT * FROM banco"))
