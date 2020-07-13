# http://quotes.toscrape.com/

from requests import get
from csv import DictWriter
from bs4 import BeautifulSoup

response = get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text, features="html.parser")
quotes = html_data.find_all(class_='quote')

with open('quotes.csv', 'w') as file:
    header_list = ['Quote', 'Author', 'Keywords']
    writer = DictWriter(file, fieldnames=header_list)
    writer.writeheader()
    for quote in quotes:
        writer.writerow({
            'Quote': quote.find(class_='text').get_text(),
            'Author': quote.find(class_='author').get_text(),
            'Keywords': quote.find(class_='keywords')['content']
        })
