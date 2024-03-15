# Scraper de Artículos con PostgreSQL

Este script en Python está diseñado para extraer información de artículos de un sitio web y almacenarla en una base de datos PostgreSQL. Utiliza la biblioteca `psycopg2` para la conexión con la base de datos y `BeautifulSoup` para el scraping del sitio web.

## Requisitos

Instalar las siguientes bibliotecas de Python:

- psycopg2
- requests
- beautifulsoup4
- logging

Intalalas usando pip:

pip install psycopg2 requests beautifulsoup4

## Configuración de la Base de Datos

Antes de ejecutar el script, asegúrate de tener una base de datos PostgreSQL configurada con los sig datos:

- Usuario
- Contraseña
- Host
- Puerto
- Nombre de la base de datos

## Funcionamiento del Script

1. **Conexión a la BD**: Conectamos a la BD ingresando los datos en el punto anterior

2. **Crear Tabla de la BD para los Articulos**: Creamos la tabla en el caso de que no exista, sin esta tabla el resto del programa no funciona (la tabla contiene --> id, titulo, fecha, contenido, url)

3. **Obtener Lista de Articulos para Scrapear**: Recorremos la pagina de inicio mientras guardamos las "url" de los articulos mas recientes

4. **Subir datos a la BD**: Recorremos la lista de articulos que obtuvimos, ingresamos a cada url (si no existe en la tabla que creamos/existe en la BD) y del articulo guardamos el titulo, fecha, contenido y la url y lo subimos a la tabla.

## Estructura del Código

- `database.py`: Es el que encarga de establecer la conexión con la base de datos y llamar a las funciones de scraping.
- `scraper.py`: Contiene las funciones para el scraping del sitio web y la manipulación de la base de datos.
