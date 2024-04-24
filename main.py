from bs4 import BeautifulSoup
import requests
import csv
import os

# Function to extract data from parsed HTML and write to CSV
def extract_data_and_write_to_csv(parsed_html):
    base_dir = '/Users/****/Documents/Code/****'
    output_csv_file_path = os.path.join(base_dir, 'menu.csv')

    with open(output_csv_file_path, 'a', newline='') as output_csv_file:
        writer = csv.writer(output_csv_file)
        for div in parsed_html.find_all('div', class_='col-md-3 card-menu'):
            # Extract items
            item_name = div.find('h5').text.strip()
            item_description = div.find('p').text.strip()
            image_url = div.find('img')['src']
            writer.writerow([item_name, item_description, image_url])

# Loop over each page of the menu. 14 is ofc hardcoded, but you can find a way to get the total number of pages
for i in range(1, 14):
    response = requests.get(f'https://remboelan.com/menu/{i}')
    soup = BeautifulSoup(response.text, 'html.parser')
    extract_data_and_write_to_csv(soup)


