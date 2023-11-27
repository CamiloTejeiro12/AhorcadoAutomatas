import psycopg2
from psycopg2 import sql
import random

# INSERT INTO palabras (palabra, pista) VALUES  ('MILIO', 'Supp con amigos de fuego'), ('KARMA', 'Portadora de los dragones espirituales de Jonia'), ('AHRI', 'ZORRA');


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


def listar_registros():
    connection, cursor = conectar()

    if connection and cursor:
        try:
            query = sql.SQL("SELECT * FROM palabras;")
            cursor.execute(query)
            results = cursor.fetchall()

            return results

        except Exception as e:
            print(f"Error al listar registros: {e}")

        finally:
            cerrar_conexion(connection, cursor)

    return None


def insertar_registro(datos):
    connection, cursor = conectar()

    if connection and cursor:
        try:
            query = sql.SQL(
                "INSERT INTO palabras (palabra, pista) VALUES (%s, %s);")
            cursor.execute(query, datos)

            # Confirmar los cambios
            connection.commit()

            print('Inserccion exitosa')

        except Exception as e:
            print(f"Error al insertar registro: {e}")

        finally:
            cerrar_conexion(connection, cursor)


def actualizar_registro(id_registro, nuevos_datos):
    connection, cursor = conectar()

    if connection and cursor:
        try:
            # Ejemplo de actualización, asumiendo que 'tu_tabla' tiene columnas 'columna1' y 'columna2'
            query = sql.SQL(
                "UPDATE palabras SET palabra = %s, pista = %s WHERE id = %s;")
            cursor.execute(query, (*nuevos_datos, id_registro))

            # Confirmar los cambios
            connection.commit()

        except Exception as e:
            print(f"Error al actualizar registro: {e}")

        finally:
            cerrar_conexion(connection, cursor)


def eliminar_registro(id_registro):
    connection, cursor = conectar()

    if connection and cursor:
        try:
            # Ejemplo de eliminación, asumiendo que 'tu_tabla' tiene una columna 'id'
            query = sql.SQL("DELETE FROM palabras WHERE id = %s;")
            cursor.execute(query, (id_registro,))

            # Confirmar los cambios
            connection.commit()

        except Exception as e:
            print(f"Error al eliminar registro: {e}")

        finally:
            cerrar_conexion(connection, cursor)


# Las funciones de conexión, cerrar conexión, listar, insertar, actualizar y eliminar se mantienen...

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
        # Desempacar los datos de la tupla en tres variables
        id_registro, palabra, pista = registro_aleatorio

        return id_registro, palabra, pista

    return None


# Ejemplo de uso desde main.py


"""
# Llamar a la función para listar registros
registros = listar_registros()

if registros:
    print("Registros:")
    for registro in registros:
        print(registro)
else:
    print("No se pudieron obtener registros.")

# Llamar a la función para insertar un nuevo registro
nuevos_datos = ('BRANDON SANDERSON', 'Autor del archivo de las tormentas')
insertar_registro(nuevos_datos)
"""


# Llamar a la función para actualizar un registro existente
"""
id_registro_a_actualizar = 1  # Supongamos que quieres actualizar el registro con ID 1
nuevos_datos_actualizados = ('Valor Actualizado 1', 'Valor Actualizado 2')
actualizar_registro(id_registro_a_actualizar, nuevos_datos_actualizados)
"""

# Llamar a la función para eliminar un registro
"""
id_registro_a_eliminar = 2  # Supongamos que quieres eliminar el registro con ID 2
eliminar_registro(id_registro_a_eliminar)
"""
