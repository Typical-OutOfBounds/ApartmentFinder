from bs4 import BeautifulSoup as soup
import requests

links = []
page = 1

def city_search(city, state):
    get_complexes('https://www.apartments.com/' + city + '-' + state + '/', page)

def get_complexes(url, page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    uClient = requests.get(url, headers = headers)
    page_html = uClient.content

    page_soup = soup(page_html, 'html.parser')

    complexes = page_soup.find('div', {'id': "placardContainer", 'class': "placardContainer"})
    complexes = complexes.select('article')

    # for sophisticated and less sophisticated listings
    for comp in complexes:
        try:
            link = comp.find('header', {'class': 'placardHeader'})
            links.append(link.a['href'])
        except:
            link = comp.a['href']
            links.append(link)


    # The next button on the website is a javascript command
    # This is the next best option for purely python w/o json

    pages = page_soup.find('p', {'class': 'searchResults'})
    range_string = pages.span.string.strip()
    temp = range_string.split()
    max_page = temp[-1]

    if int(max_page) > 1:
        while page < int(max_page):
            if page == 1:

                page += 1
                get_complexes(url+str(page)+'/',page)
                return

            else:
                page += 1
                url_parts = list(url)

                if page > 10:
                    del url_parts[-1]

                del url_parts[-1]
                url_parts[-1] = page
                url_parts.append('/')
                get_complexes("".join(str(item) for item in url_parts), page)
                return

