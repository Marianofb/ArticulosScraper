import logging
import click
import psycopg2

import config 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@click.group()
def cli():
    pass

@cli.command(help="Obtener los datos de la tabla de articulos.")
def obtenerDatosTabla():
    try:
        connection = psycopg2.connect(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tablaDatos")
        records = cursor.fetchall()

        for record in records:
            print(f"ID: {record[0]}")
            print(f"URL: {record[4]}")
            print(f"TÍTULO: {record[1]}")
            print(f"FECHA: {record[2]}")
            print(f"CONTENIDO: {record[3]}")
            print("-" * 50)


    except psycopg2.Error as e:
        logger.error("Error al conectar a la base de datos o al leer la configuración: %s", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    cli()
