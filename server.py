import psycopg2
import scraper
from psycopg2 import Error

url = 'http://www.mindefensa.gob.ve/mindefensa/2016/06/10/armada-bolivariana-realizo-con-exito-ejercicio-conjunto-patria-chavista-ii-2016/'
#CAUSA ERROR
#http://www.mindefensa.gob.ve/mindefensa/2019/12/14/mensaje-del-gj-vladimir-padrino-lopez-con-motivo-de-celebrarse-el-41o-aniversario-del-comando-de-defensa-aeroespacial-integral-codai/

def crearTabla(connection):
    try:
        crear_tabla_query = '''
        CREATE TABLE IF NOT EXISTS  tablaDatos (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            fecha DATE,
            contenido TEXT,
            url TEXT
        )
        '''
        cursor = connection.cursor()
        cursor.execute(crear_tabla_query)
        connection.commit()

    except Exception as e:
        print("ERROR: al crear la tabla", e)

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
    print("ERROR: al conectarse a PostgreSQL:", e)

finally:
    if connection:
        print("EXTIO: conectamos con la BD --> " + connection.info.dbname)
        crearTabla(connection)
        scraper.subirDatos(connection, url)
        cursor.close()
        print("FINALIZAR: cerrar la conexion con la BD --> " + connection.info.dbname)
        connection.close()

