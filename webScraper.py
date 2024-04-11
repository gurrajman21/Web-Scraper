import requests
from bs4 import BeautifulSoup
import csv

# Web scraping function to scrape quotes 
def quote_scraper(url, document):
    # Opens the csv file in write mode
    with open(document, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Quote', 'Author', 'Tags'])

        # Sends HTTP request to the url specified
        response = requests.get(url)

        # Checks if the HTTP request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve url: {url}")
            return

        # Parses the HTML of the website
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finds all quote containers on the page
        quotes = soup.find_all('div', class_='quote')

        # Extracts the quote, author and tags and then writes to the csv file
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = ', '.join(tag.text for tag in quote.find_all('a', class_='tag'))
            writer.writerow([text, author, tags])


# Example usage of the web scraping function
url = "http://quotes.toscrape.com"
file = "text.csv"
quote_scraper(url, file)