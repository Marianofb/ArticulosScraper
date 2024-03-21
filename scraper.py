import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        logger.error("Al crear la tabla: %s", e)

def recorrerArticulos(connection, url_inicio):
    try:
        pagina = requests.get(url_inicio)

        if pagina.status_code == 200:
            soup = BeautifulSoup(pagina.text, 'html.parser')
    
            articulos = soup.find_all("h3", attrs={"class": "vw-post-box-title"})
            logger.info("Total de artículos encontrados: %d", len(articulos))
            
            for articulo in articulos:
                a = articulo.find('a')
                url = a.get('href') 
                
                if not existeURLBD(connection, url):
                    subirDatosArticulo(connection, url)
                else:
                    logger.info("La URL ya existe en la base de datos: %s", url)

    except Exception as e:
        logger.error("Al recorrer los artículos: %s", e)

def existeURLBD(connection, url):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM tablaDatos WHERE url = %s)", (url,))
        exists = cursor.fetchone()[0]
        cursor.close()
        return exists
    except Exception as e:
        logger.error("Al verificar la existencia de la URL en la base de datos: %s", e)
        return False

def subirDatosArticulo(connection, url):
    try:
        pagina = requests.get(url)

        if pagina.status_code == 200:
            soup = BeautifulSoup(pagina.text, 'html.parser')

            dia = soup.find_all("span", attrs={"class": "vw-date-box-date"})
            mesAño = soup.find_all("span", attrs={"class": "vw-date-box-month"})
            titulo = soup.find_all("h1", attrs={"class": "entry-title"})

            mes = mesAño[0].text.split()[0]
            año = mesAño[0].text.split()[1]

            t = titulo[0].text
            mes = traducirMesEspañolIngles(mes)
            fecha = dia[0].text + "/" + mes + "/" + año

            parrafos = soup.find_all("div", attrs={"class": "vw-post-content clearfix"})
            texto = parrafos[0].text

            insert_query = "INSERT INTO tablaDatos (titulo, fecha, contenido, url) VALUES (%s, %s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(insert_query, (t, fecha, texto, url))
            connection.commit()
            logger.info("Datos insertados correctamente.")

    except Exception as e:
        logger.error("Al subir datos a la tabla: %s", e)

def traducirMesEspañolIngles(mes):
    try:
        if mes == "Dic":
            return "Dec"
        elif mes == "Ene":
            return "Jan"
        else:
            return mes 
    except Exception as e:
        logger.error("Al traducir mes: %s", e)
