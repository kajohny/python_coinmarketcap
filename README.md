# WEB SCRAPING FROOM COINMARKETCAP WITH PYTHON

## Installation
```
import requests
```
```
from bs4 import BeautifulSoup
```
## Usage
```
import requests
from bs4 import BeautifulSoup
site = requests.get('https://coinmarketcap.com/currencies/' + name)
soup = BeautifulSoup(site.content,'html.parser')
```
## Examples

```
soup.find_all('p')
soup.find('p').text
for link in soup.find_all('a'):
    print(link.get('href'))
```

*Showing related data to cryptocurrency*:

**Input**: 
```
bitcoin
```
**Output**:
```
"Name": bitcoin, "Symbol": BTC, "Market Cap": $1,040,140,595,227, "Price": $55,208.94, "Circulating Supply": 18,840,075.00 BTC, "Volume": $35,470,617,443
```

*Providing a list of paragraphs*

**Input**:
```
bitcoin
```
**Output**:
```
The live Bitcoin price today is $55,208.94 USD with a 24-hour trading volume of $35,470,617,443 USD. We update our BTC to USD price in real-time. Bitcoin is up 0.64% in the last 24 hours. The current CoinMarketCap ranking is #1, with a live market cap of $1,040,140,595,227 USD. It has a circulating supply of 18,840,075 BTC coins and a max. supply of 21,000,000 BTC coins.
If you would like to know where to buy Bitcoin, the top exchanges for trading in Bitcoin are currently Binance, Huobi Global, Mandala Exchange, OKEx,  and FTX. You can find others listed on our crypto exchanges page.
Bitcoin is a decentralized cryptocurrency originally described in a 2008 whitepaper by a person, or group of people, using the alias Satoshi Nakamoto. It was launched soon after, in January 2009.
Bitcoin is a peer-to-peer online currency, meaning that all transactions happen directly between equal, independent network participants, without the need for any intermediary to permit or facilitate them. Bitcoin was created, according to Nakamoto’s own words, to allow “online payments to be sent directly from one party to another without going through a financial institution.”
Some concepts for a similar type of a decentralized electronic currency precede BTC, but Bitcoin holds the distinction of being the first-ever cryptocurrency to come into actual use.
Bitcoin’s original inventor is known under a pseudonym, Satoshi Nakamoto. As of 2021, the true identity of the person — or organization — that is behind the alias remains unknown.
On October 31, 2008, Nakamoto published Bitcoin’s whitepaper, which described in detail how a peer-to-peer, online currency could be implemented. They proposed to use a decentralized ledger of transactions packaged in batches (called “blocks”) and secured by cryptographic algorithms — the whole 
system would later be dubbed “blockchain.”
```
