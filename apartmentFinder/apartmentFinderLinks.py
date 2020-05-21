from bs4 import BeautifulSoup as soup
import requests

url = 'https://www.apartmentfinder.com/Michigan/East-Lansing-Apartments'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
uClient =requests.get(url, headers=headers)
page_html = uClient.content

page_soup = soup(page_html, 'html.parser')
