import psycopg2
import scraper
from psycopg2 import Error
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
    logger.info("Versión del servidor PostgreSQL: %s", record)

except (Exception, Error) as e:
    logger.error("Al conectarse a PostgreSQL: %s", e)

finally:
    if connection:
        logger.info("CONECTANDO con la BD --> %s", connection.info.dbname)
        #Ejecutar database.crearTabla() solo una vez para que pueda funcionar el resto del programa
            #database.crearTabla(connection)
        scraper.recorrerArticulos(connection, url_inicio)
        cursor.close()
        logger.info("CERRANDO la conexion con la BD --> %s", connection.info.dbname)
        connection.close()

