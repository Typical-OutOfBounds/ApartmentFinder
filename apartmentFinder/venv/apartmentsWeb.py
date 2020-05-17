from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from bs4 import NavigableString
import requests

my_url = "https://www.apartments.com/castle-pointe-east-lansing-mi/ybf975v/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
bedrooms = 1

uClient = requests.get(my_url,headers = headers)
page_html = uClient.content