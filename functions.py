import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime


def get_usdprice_and_date(url = str) -> tuple:
    '''
    Get the price in USD and 'Fecha de publicacion'. 
    As this values are found on different urls, this scrapper should be implemented in a loop, 
    meaning that this function will be used to make multiple requests 
    (execution time can take a while).

    Returns price and date in bs4.NavigableString format.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    sleep(1)
    # Tag where usd price is
    price_wrapper = soup.find('div', class_='price-wrapper')
    us_price = price_wrapper.find_next_sibling('span').span.string
    # tag where publication date is
    fecha = (
        soup.find('table', class_='woocommerce-product-attributes')
        .find('th', string='Fecha de publicación')
        .find_next_sibling('td').p.string
    )
    return us_price, fecha

def format_date(date=str, old_format=str, new_format: str='d%/%m/%Y'):
    """Changes date format and returns it as a string."""
    obj_date = datetime.strptime(date, old_format)
    return obj_date.strftime(new_format)


# def get_pub_date(url = str):
#     '''
#     Get the publicacion date posted on curren Book's url.
#     As dates are found on different url's, this scrapper should be used in a loop, 
#     meaning that it'll be used to make multiple requests 
#     (execution time can take a while).

#     Returns date in bs4.NavigableString format.
#     '''
#     r = requests.get(url)
#     s = BeautifulSoup(r.content, 'html.parser')

#     fecha = (
#         s.find('table', class_='woocommerce-product-attributes')
#         .find('th', string='Fecha de publicación')
#         .find_next_sibling('td').p.string
#     )
#     return fecha