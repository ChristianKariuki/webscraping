import random
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

webpage = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')


print(soup.title.text)


crypto_rows = soup.find_all('tr')[1:6]  
for index, row in enumerate(crypto_rows, start=1):
    cells = row.find_all('td')  
    if len(cells) > 4: 
        name = cells[2].get_text(strip=True)  
        symbol = cells[3].get_text(strip=True)  
        price = cells[4].get_text(strip=True)
        change_24h = cells[5].get_text(strip=True) 

        print(f"Top {index}: {name} ({symbol})")
        print(f"Current Price: {price}")
        print(f"Change (24h): {change_24h}")
        print('-' * 30)
