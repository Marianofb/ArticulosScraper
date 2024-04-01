# Scraper de Artículos con PostgreSQL

Este script en Python está diseñado para extraer información de artículos de un sitio web y almacenarla en una base de datos PostgreSQL. Utiliza la biblioteca `psycopg2` para la conexión con la base de datos, `BeautifulSoup` para el scraping del sitio web y `click` para poder visualizar en la consola los ultimos datos que guardamos en la BD.

## Requisitos

Instalar las siguientes bibliotecas de Python:

- psycopg2
- requests
- beautifulsoup4
- click
- logging

Utilizando el siguiente comando:

pip install psycopg2 requests beautifulsoup4 click

## Configuración de la Base de Datos

Estos son los datos que establecemos en el config.py y  que vamos a utilizar para conectar a la base de datos:

- Usuario
- Contraseña
- Host
- Puerto
- Nombre de la base de datos

## Funcionamiento del Script

1. **Conexión a la BD**: Conectamos a la BD ingresando los datos en el punto anterior
2. **Crear Tabla de la BD para los Articulos**: Creamos la tabla en el caso de que no exista, sin esta tabla el resto del programa no funciona (la tabla contiene --> id, titulo, fecha, contenido, url)
3. **Obtener Lista de Articulos para Scrapear**: Recorremos la pagina de inicio mientras guardamos las "url" de los articulos mas recientes
4. **Subir datos a la BD**: Recorremos la lista de articulos que obtuvimos, ingresamos a cada url (si no existe esa url en la tabla que creamos en la BD) y del articulo guardamos el titulo, fecha, contenido y la url y lo subimos a la tabla.
5. **Visualizar datos de la BD**: Con el comando "python main.py obtenerdatostabla" podemos visualizar en la consola lo que contiene la tabla de la BD

## Estructura del Código

- `config.py`: Contiene los datos que nos permiten conectar a la BD.
- `database.py`: Es el que encarga de establecer la conexión con la base de datos y llamar a las funciones de scraping.
- `scraper.py`: Contiene las funciones para el scraping del sitio web y la manipulación de la base de datos.
- `main.py`: Me permite visualizar los datos de la tabla de la DB a traves de un comando desde la consola.
