# Beautiful Remboelan

This project scrapes the menu from the Remboelan website and saves the data to a CSV file.

## Files

- `main.py`: This is the main script that scrapes the website and writes the data to a CSV file.
- `menu.csv`: This CSV file contains the scraped data. Each row represents a menu item and has three columns: the item name, the item description, and the URL of the item image.
- `notion.py`: This script contains a function to push data to a Notion database.

## How to Run

1. Install the required Python packages with `pip install -r requirements.txt` (you'll need to create this file with the packages: `beautifulsoup4`, `requests`, `lxml`).
2. Run the `main.py` script with `python main.py`.

## Note

This project is intended for educational purposes only.
