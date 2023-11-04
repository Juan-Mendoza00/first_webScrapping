import requests
from bs4 import BeautifulSoup
import pymysql
from time import sleep

from functions import get_usdprice_and_date, format_date

# Dolar Blue price
print('Obteniendo precio de Dolar Blue...')
r = requests.get('https://www.cronista.com/MercadosOnline/dolar.html', timeout=5)
dom_content = r.text
html_soup = BeautifulSoup(dom_content, 'html.parser')
dolar_blue = html_soup.find('span', string='Dólar Blue')
dolar_blue.next_sibling.text[1:]
dolarBlue_price = float(dolar_blue.next_sibling.text[1:].replace(",","."))
print(f'Precio Dolar Blue: {dolarBlue_price}')

# HTTP request for scrapping website
print('Procediendo a obtener el Listado de libros.')
url = 'https://cuspide.com/100-mas-vendidos/' 
response = requests.get(url, timeout=5) 
html_content = response.content

# Parsing with bs4
soup = BeautifulSoup(html_content, 'html.parser')
title_tags = soup.find_all("h3", class_='product-title')

table = []
error_table = []
# Loop over every tag obtained
for tag in title_tags:
    title = tag.get_text(strip=True).title()
    print(f'*****\nObteniendo información del libro: \n-> {title}')
    url = tag.a.attrs['href']
    # Tag for price
    price = (
        tag.find_next_sibling("div", "product-price")
        .get_text(strip=True))
    # Format and cast
    price = float(price[1:].replace(".","").replace(",","."))
    try:
        # Function to get usd price within every book's window
        usd_price, pub_date = get_usdprice_and_date(url)
        usd_price = float(usd_price.replace(",","."))
        blue_price = round(price / dolarBlue_price, 2)
        # Change date format to SQL date format
        pub_date = format_date(pub_date, old_format='%d/%m/%Y', new_format='%Y-%m-%d')
        table.append(
            (title, pub_date, url, price, usd_price, blue_price))
    except:
        requests.HTTPError
        print(f'ERROR AL SCRAPEAR')
        error_table.append(
            (title, url)
        )
print('Libros scrapeados exitosamente:', len(table))
print('Libros no scrapeados:', len(error_table))
print('\nInciando conexión con base de datos y ejecutando inserción\nde datos recopilados.')
sleep(2)
# Creating MySQL connection
connection = pymysql.Connection(
    host='localhost',
    user='juancml',
    passwd='',
    database='libros'
)
# creating mysql cursor
cursor = connection.cursor()
query = """
INSERT INTO libros_semana (Titulo,Fecha_Publicación,URL,Precio,Precio_USD,Precio_DolarBlue,Fecha_carga)
VALUES (%s,%s,%s,%s,%s,%s, CURDATE())
"""
# Inserting data
cursor.executemany(query, table)
if len(error_table) > 0:
    cursor.executemany("INSERT INTO auditoria_errores VALUES(%s,%s)", error_table)
connection.commit()
connection.close()
sleep(2)
print('''Consulta SQL reallizada.\n
      VERIFIQUE QUE NO HAYA ERROES.\n
      Proceso terminado :)''')