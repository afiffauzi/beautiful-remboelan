from bs4 import BeautifulSoup
import requests

def print_div(soup):
    for div in soup.find_all('div', class_='col-md-3 card-menu'):
        item_name = div.find('h5').text.strip()
        item_description = div.find('p').text.strip()

        print(f'Item Name: {item_name}')
        print(f'Item Description: {item_description}')
        print('------------------------')

for i in range(1, 14):
    response = requests.get(f'https://remboelan.com/menu/{i}')
    soup = BeautifulSoup(response.text, 'html.parser')
    print_div(soup)


