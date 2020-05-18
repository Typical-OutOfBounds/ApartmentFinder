from bs4 import BeautifulSoup as soup
import requests

my_url = "https://www.apartments.com/castle-pointe-east-lansing-mi/ybf975v/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
bedrooms = 1

uClient = requests.get(my_url,headers = headers)
page_html = uClient.content

bed_val = "bed" + str(bedrooms)
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
print(address)

apartments = page_soup.find('div', {'data-tab-content-id':bed_val})

available = apartments.div.table.tbody


rooms = [item for item in available.select('tr[data-beds=\"'+str(bedrooms)+'\"]')]

to_rent = []
for item in rooms:
    to_rent.append({item['data-rentalkey']:[item['data-maxrent'], item['data-model']]})

print(to_rent)