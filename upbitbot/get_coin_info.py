from matplotlib import ticker
from matplotlib.pyplot import get
import pyupbit
import time
import requests
import json
import operator
import requests
import time

from bs4 import BeautifulSoup
from import_module import *
from asyncore import loop
# get_all_ticker not include "KRW"
def get_all_ticker():
    max_count = -1
    try:
        while True:
            ticker_list = pyupbit.get_tickers(fiat="KRW")
            max_count = max_count + 1
            time.sleep(0.05)
            
            if max_count >= len(ticker_list)-1:
                break

    except Exception:
        raise
    return ticker_list

# processing time = 20 sec
# return coin ticker
def get_filtered_ticker(value):
    ticker_price = []
    ticker_name = []
    name = get_all_ticker()
    max_count = 0
    try:
        while True:
            ticker_price.append(int(pyupbit.get_current_price(name[max_count])))
            
            if 1000 < ticker_price[max_count] < value:
                ticker_name.append(name[max_count])
            
            max_count = max_count + 1
            if max_count >= len(name)-1:
                break
            time.sleep(0.05)
    except Exception:
        raise
    
    return ticker_name, ticker_price

# Get top 10% trading volume
def get_trade_volume(value):
    acc_trade_result = dict()
    change_rate = dict()
    max_count = 0
    loop_count = 0
    ticker_name, ticker_price = get_filtered_ticker(value) # return dictionary
    try:
        while True:
            
            url = "https://api.upbit.com/v1/ticker?markets=" + ticker_name[max_count]
            headers = {"Accept": "application/json"}
            response = requests.request("GET", url, headers=headers).json()
        
            trade_value = json.loads(json.dumps(response, indent=4))
            
            time.sleep(0.2)
            
            if trade_value[0]['change'] == 'RISE':
                acc_trade_result[ticker_name[max_count]] = round(trade_value[0]['acc_trade_volume_24h'], 8)
                change_rate[ticker_name[max_count]] = round(trade_value[0]['signed_change_rate'], 3)*100
            
            loop_count = loop_count + 1
            max_count = max_count + 1
            if loop_count > len(ticker_name)-1:
                break
    except Exception:
        raise

    change_rate = sorted(change_rate.items(), key=operator.itemgetter(1), reverse=True)
    acc_trade_result = sorted(acc_trade_result.items(), key=operator.itemgetter(1), reverse=True)

    return change_rate, acc_trade_result

# get krw balance
def get_my_balance():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)
    balance = int(float(res.json()[0]['balance']))
    return balance

def get_my_coin_balance():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)

    balance = res.json()
    return balance

# ref : https://www.tradingbro.co.kr/t/topic/88/2
def toptrade():
    url = "https://www.coingecko.com/ko/거래소/upbit"
    resp = requests.get(url)

    bs = BeautifulSoup(resp.text,'html.parser')
    selector = "tbody > tr > td > a"
    columns = bs.select(selector)

    ticker_in_krw = [x.text.strip() for x in columns if x.text.strip()[-3:] == "KRW"]
    ticker = list()
    for i in range(0, len(ticker_in_krw)):
        ticker.append(ticker_in_krw[i].split('/')[0])
    
    return ticker

def get_trade_rate(ticker):
    url = f"https://api.upbit.com/v1/ticker?markets=KRW-{ticker}"
    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers).json()
    return round(response[0]['signed_change_rate'],2)
