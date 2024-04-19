from bs4 import BeautifulSoup
import requests
import csv

def print_div(soup):
    with open('/Users/afiffauzi/Documents/Code/beautiful-remboelan/menu.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for div in soup.find_all('div', class_='col-md-3 card-menu'):
            item_name = div.find('h5').text.strip()
            item_description = div.find('p').text.strip()
            writer.writerow([item_name, item_description])

for i in range(1, 14):
    response = requests.get(f'https://remboelan.com/menu/{i}')
    soup = BeautifulSoup(response.text, 'html.parser')
    print_div(soup)


