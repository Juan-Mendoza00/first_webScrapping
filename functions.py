import requests
from bs4 import BeautifulSoup


def get_us_price(url = str):
    '''
    Get the price in USD.
    As prices are found on different url's, this scrapper should be implemented in a loop, 
    meaning that this function will be used to make multiple requests 
    (execution time can take a while).

    Returns price in bs4.NavigableString format.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    price_wrapper = soup.find('div', class_='price-wrapper')
    us_price = price_wrapper.find_next_sibling('span').span.string

    return us_price

def get_pub_date(url = str):
    '''
    Get the publicacion date posted on curren Book's url.
    As dates are found on different url's, this scrapper should be used in a loop, 
    meaning that it'll be used to make multiple requests 
    (execution time can take a while).

    Returns date in bs4.NavigableString format.
    '''
    r = requests.get(url)
    s = BeautifulSoup(r.content, 'html.parser')

    fecha = (
        s.find('table', class_='woocommerce-product-attributes')
        .find('th', string='Fecha de publicación')
        .find_next_sibling('td').p.string
    )
    return fecha