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

    def query(self, query, params=None):
        cnx = mysql.connector.connect(**self.__configuration)
        cursor = cnx.cursor()

        if params == None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

        result = []
        for data_result in cursor:
            result.append(data_result)

        cursor.close()
        cnx.close()

        return result


database = Database()

# devuelve una lista vacía
print(database.query("select * from banco where nombre = %s", ('Santaner',)))


# Devuelve todos los bancos
print(database.query("select * from banco"))
