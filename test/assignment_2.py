import requests
from bs4 import BeautifulSoup

site = requests.get('https://coinmarketcap.com/currencies/bitcoin')
soup = BeautifulSoup(site.content,'html.parser')
print(soup.find_all('p')
print(soup.find('p', class_ = 'esfl2f-0 kqzSsi')
