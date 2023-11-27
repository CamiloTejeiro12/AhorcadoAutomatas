import psycopg2
from psycopg2 import sql
import random


def conectar():
    # Configuración de la conexión a la base de datos
    db_config = {
        'host': 'localhost',
        'database': 'ahorcado',
        'user': 'postgres',
        'password': 'postgres',
        'port': '5432',  # Por lo general, el puerto predeterminado es 5432
    }

    try:
        # Conectar a la base de datos
        connection = psycopg2.connect(**db_config)

        # Crear un objeto cursor para ejecutar consultas
        cursor = connection.cursor()

        print('Conexión exitosa')

        return connection, cursor

    except Exception as e:
        print(f"Error de conexión: {e}")
        return None, None


def cerrar_conexion(connection, cursor):
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()


def seleccionar_registro_aleatorio():
    connection, cursor = conectar()

    if connection and cursor:
        try:
            # Ejemplo de selección aleatoria
            query = sql.SQL(
                "SELECT * FROM palabras ORDER BY RANDOM() LIMIT 1;")
            cursor.execute(query)

            result = cursor.fetchone()
            return result

        except Exception as e:
            print(f"Error al seleccionar registro aleatorio: {e}")

        finally:
            cerrar_conexion(connection, cursor)

    return None

# Las funciones de conexión, cerrar conexión, listar, insertar, actualizar y eliminar se mantienen...


def dividir_registro_aleatorio():
    # Obtener un registro aleatorio desde la base de datos
    registro_aleatorio = seleccionar_registro_aleatorio()

    if registro_aleatorio:
        # Dividir los datos del registro en tres partes
        id_registro, palabra, pista = registro_aleatorio

        # Realizar el proceso de división según tus necesidades
        longitud_palabra = len(palabra)
        parte1 = palabra[:longitud_palabra // 3]
        parte2 = palabra[longitud_palabra // 3: 2 * (longitud_palabra // 3)]
        parte3 = palabra[2 * (longitud_palabra // 3):]

        return parte1, parte2, parte3, pista

    return None
