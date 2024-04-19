from bs4 import BeautifulSoup
import requests
import csv
import os

def print_div(soup):
    base_dir = '/Users/****/Documents/Code/****'
    output_file = os.path.join(base_dir, 'menu.csv')

    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for div in soup.find_all('div', class_='col-md-3 card-menu'):
            item_name = div.find('h5').text.strip()
            item_description = div.find('p').text.strip()
            writer.writerow([item_name, item_description])

for i in range(1, 14):
    response = requests.get(f'https://remboelan.com/menu/{i}')
    soup = BeautifulSoup(response.text, 'html.parser')
    print_div(soup)


