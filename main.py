from bs4 import BeautifulSoup
import requests
import csv
import os
import time

# Function to extract data from parsed HTML and write to CSV
def extract_data_and_write_to_csv(parsed_html):
    base_dir = '/Users/Afiffauzi/Documents/Code/beautiful-remboelan'
    output_csv_file_path = os.path.join(base_dir, 'menu.csv')

    with open(output_csv_file_path, 'a', newline='') as output_csv_file:
        writer = csv.writer(output_csv_file)
        for div in parsed_html.find_all('div', class_='col-md-3 card-menu'):
            # Extract items
            item_name = div.find('h5').text.strip()
            item_description = div.find('p').text.strip()
            image_url = div.find('img')['src']
            writer.writerow([item_name, item_description, image_url])

def main():
    base_url = 'https://remboelan.com/menu/{}'
    page_number = 1
    while True:
        url = base_url.format(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if the page contains any menu items. Temporarily hardoced the class name
        menu_items = soup.find_all('div', class_='col-md-3 card-menu')
        if not menu_items:
            break  # No more pages

        extract_data_and_write_to_csv(soup)
        page_number += 1
        print(page_number)
        time.sleep(5)  # Optional: sleep for a bit between requests to avoid overloading the server

if __name__ == "__main__":
    main()


