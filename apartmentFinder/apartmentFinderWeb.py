from bs4 import BeautifulSoup as soup
import requests

my_url = "https://www.apartmentfinder.com/Michigan/East-Lansing-Apartments/Castle-Pointe-Apartments"
bedrooms = 1

def find_data(beds, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    uClient = requests.get(url, headers=headers)
    page_html = uClient.content

    bed_val = "bed" + str(beds)
    page_soup = soup(page_html, "html.parser")

    address = page_soup.find('div', {'class': "address"})
    address = address.span.string

    name = page_soup.find('div', {'class': "name"})
    name = name.h1.string.strip()

    to_rent = [name, address]

    try:
        apartments = page_soup.find('div', {"data-tab-content-id": bed_val})
        available = apartments.div

        rooms = [item for item in available.select('div[data-beds=\"' + str(beds) + '\"]')]


        for item in rooms:
            to_rent.append({item['data-rentalkey']: [item['data-maxrent'], item['data-model']]})

    except:
        to_rent.append("No rooms available")

    return to_rent

print(find_data(bedrooms, my_url))