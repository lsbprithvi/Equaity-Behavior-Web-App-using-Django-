import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request('https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(webpage, "html.parser")
result = soup.find(id="ContentPlaceHolder1_btnhylZip")
print(result['href'])

