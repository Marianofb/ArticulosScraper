import requests
from bs4 import BeautifulSoup

def subirDatos(connection, url):
    try:
        pagina = requests.get(url)

        if pagina.status_code == 200:
            soup = BeautifulSoup(pagina.text, 'html.parser')

            #Titulo/Fecha
            dia = soup.find_all("span", attrs = {"class" : "vw-date-box-date"})
            mesAño = soup.find_all("span", attrs = {"class" : "vw-date-box-month"})
            titulo = soup.find_all("h1", attrs = {"class" : "entry-title"})

            mes = mesAño[0].text.split()[0]
            año = mesAño[0].text.split()[1]
            
            t = titulo[0].text
            fecha =  dia[0].text + "/" + mes + "/" + año

            #Contenido
            parrafos = soup.find_all("div", attrs = {"class" : "vw-post-content clearfix"})
            texto = parrafos[0].text

            insert_query = "INSERT INTO tablaDatos (titulo, fecha, contenido, url) VALUES (%s, %s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(insert_query, (t, fecha, texto, url))
            connection.commit()
            print("Datos insertados correctamente.")

    except Exception as e:
        print("ERROR: al subir datos a la tabla:", e)