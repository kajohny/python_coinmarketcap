import requests
from bs4 import BeautifulSoup

class ScrapingTool:
    def __init__(self):
        pass

    def getParagraphList(self, name):
        pList = soup.find_all('p')
        for lists in pList[:-2]:
            print(lists.text)

    def getData(self, name):
        symbol = soup.find('small', class_= 'nameSymbol').text
        marketCap = soup.find('div', class_ = 'statsValue').text
        price = soup.find('div', class_= 'priceValue').text
        volumes = soup.find_all('div', class_ = 'statsValue')
        for volume in volumes[2]:
            volume.text
        circulatingSupply = soup.find('div', class_ = 'sc-16r8icm-0 inUVOz').find('div', class_ = 'statsValue').text
        print('"Name": ' + name + ', "Symbol": ' + symbol + ', "Market Cap": ' + marketCap + 
            ', "Price": ' + price + ', "Circulating Supply": ' + circulatingSupply + ', "Volume": ' + volume.text)   

scraper = ScrapingTool() 
print('Enter the name of the cryptocurrency with which you want to see the information: ')
name = input()
site = requests.get('https://coinmarketcap.com/currencies/' + name)
soup = BeautifulSoup(site.content,'html.parser')
print('What do you want?')
print('1. I want to see all paragraph lists with this cryptocurrency')
print('2. I want to see all the related information about this cryptocurrency')
n = input()
if n == '1':
    scraper.getParagraphList(name)
elif n == '2':
    scraper.getData(name)
else:
    print('You are entered wrong input!')