import requests
from bs4 import BeautifulSoup
# import pymysql

from functions import get_us_price, get_pub_date

# Dolar Blue price
print('Obteniendo precio de Dolar Blue...')
r = requests.get('https://www.cronista.com/MercadosOnline/dolar.html', timeout=2)
dom_content = r.text
html_soup = BeautifulSoup(dom_content, 'html.parser')
dolar_blue = html_soup.find('span', string='Dólar Blue')
dolar_blue.next_sibling.text[1:]
dolarBlue_price = float(dolar_blue.next_sibling.text[1:].replace(",","."))
print(f'Precio Dolar Blue: {dolarBlue_price}')

# HTTP request for scrapping website
print('Procediendo a obtener el Listado de libros.')
url = 'https://cuspide.com/100-mas-vendidos/' 
response = requests.get(url, timeout=3) 
html_content = response.content

# Parsing with bs4
soup = BeautifulSoup(html_content, 'html.parser')
title_tags = soup.find_all("h3", class_='product-title')

# Lists to keep data scrapped
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
        usd_price = get_us_price(url)
        usd_price = float(usd_price.replace(",","."))
        blue_price = round(price / dolarBlue_price, 2)
        # Function to get publication date
        pub_date = get_pub_date(url)

        table.append(
            (title, url, price, usd_price, blue_price, pub_date))
    except:
        requests.HTTPError
        print(f'ERROR AL SCRAPEAR')
        error_table.append(
            (title, url)
        )
print('Libros scrapeados exitosamente:', len(table))
print('Libros no scrapeados:', len(error_table))
print(table[:6])