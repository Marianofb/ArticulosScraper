import psycopg2
import database
from psycopg2 import Error

url_inicio = 'https://www.mindefensa.gob.ve/mindefensa/'

try:
    # Conectarse al servidor PostgreSQL
    connection = psycopg2.connect(
        user="postgres",
        password="Nutricional",
        host="localhost",
        port="5432",
        database="ApreScrapear"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Versión del servidor PostgreSQL:", record)


except (Exception, Error) as e:
    print("Al conectarse a PostgreSQL:", e)

finally:
    if connection:
        print("Conectamos con la BD --> " + connection.info.dbname)
        #Ejecutar database.crearTabla() solo una vez para que pueda funcionar el resto del programa
            #database.crearTabla(connection)
        database.recorrerArticulos(connection, url_inicio)
        cursor.close()
        print("FINALIZAR: cerrar la conexion con la BD --> " + connection.info.dbname)
        connection.close()

