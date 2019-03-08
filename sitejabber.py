from bs4 import BeautifulSoup
import requests

company = 'airbnb.com'
page = 1
rating = 1
url = f'https://www.sitejabber.com/reviews/{company}?page={page}&rating={rating}#reviews'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
