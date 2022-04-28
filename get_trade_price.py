import requests
from bs4 import BeautifulSoup
import time

def get_trading_volume():
    webpage = requests.get("https://coinmarketcap.com/ko/exchanges/upbit/")
    soup = BeautifulSoup(webpage.content, "html.parser")

    data = []
    table = soup.find('table', attrs={'class':'h7vnx2-2'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    
    return data
