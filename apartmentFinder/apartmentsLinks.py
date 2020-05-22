from bs4 import BeautifulSoup as soup
import requests

links = []

def city_search(city, state):
    pass

def get_complexes(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    uClient = requests.get(url, headers = headers)
    page_html = uClient.content

    page_soup = soup(page_html, 'html.parser')

    complexes = page_soup.find('div', {'id': "placardContainer"})
    complexes = complexes.select('article')


    for comp in complexes:
        link = comp.find('header', {'class': 'placardHeader'})
        links.append(link.a['href'])

    pages = page_soup.find('nav', {'id': 'paging'})
    nex_page = pages.find('a', {'class': 'next'})

get_complexes('https://www.apartments.com/east-lansing-mi/')