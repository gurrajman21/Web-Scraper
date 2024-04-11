# Quotes Scraper to CSV

## Project Overview

This Python script is designed to scrape quotes from `http://quotes.toscrape.com`, a website created for the purpose of practicing web scraping. The script extracts quotes, their authors, and associated tags, then saves this data into a CSV file named `quotes.csv`. This project serves as a demonstration of basic web scraping and file handling capabilities in Python.

## Features

- Fetch quotes along with their authors and tags from the first page of `http://quotes.toscrape.com`.
- Save the scraped data into a CSV file with proper headers.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library

These can be installed via pip if you do not already have them:

`pip install requests beautifulsoup4`


## Setup

1. Clone this repository or download the source code to your local machine.
2. Navigate to the directory containing the script.

## Running the Script

To run the script, open a terminal or command prompt, navigate to the script's directory, and execute:

`python webScraper.py`


Upon successful execution, a file named `text.csv` will be created in the same directory, containing the scraped quotes, authors, and tags.

## CSV File Format

The generated CSV file will have the following columns:

- **Quote**: The text of the quote.
- **Author**: The author of the quote.
- **Tags**: Tags associated with the quote, separated by commas.

## Legal and Ethical Considerations

The script is designed to scrape data from a website intended for practicing web scraping skills. Always ensure you have permission to scrape from websites and adhere to their `robots.txt` file and terms of service.

Use the script responsibly and ethically. Do not use it to scrape sensitive or personal data without consent, and do not overwhelm the website's server with requests.

## Contributing

Contributions to improve the script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

