from bs4 import BeautifulSoup as soup
import requests


def find_data(beds, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    uClient = requests.get(url, headers=headers)
    page_html = uClient.content

    bed_val = "bed" + str(beds)
    page_soup = soup(page_html, "html.parser")
    addressTag = page_soup.find('div', {'class': "propertyAddress"})
    addressTag = addressTag.h2

    address = ""
    for child in addressTag.contents:
        if child.string.strip() != ",":
            address += " " + child.string.strip()
        else:
            address += child.string.strip()
    address = address.strip()

    name = page_soup.find('h1', {'class':'propertyName'})
    name = name.string.strip()

    apartments = page_soup.find('div', {'data-tab-content-id': bed_val})

    to_rent2 = [name, address]

    try:
        available = apartments.div.table.tbody

        rooms = [item for item in available.select('tr[data-beds=\"' + str(beds) + '\"]')]


        for item in rooms:
            to_rent2.append({item['data-rentalkey']: [item['data-maxrent'], item['data-model']]})

    except AttributeError:
        to_rent2.append("No rooms available")

    return to_rent2
