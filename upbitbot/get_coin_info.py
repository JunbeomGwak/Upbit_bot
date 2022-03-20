import pyupbit
import time
import requests
import json
import operator

from tkinter import E
from datetime import datetime
# get_all_ticker not include "KRW"
def get_all_ticker():
    max_count = -1
    ticker_list = list()
    try:
        while True:
            tickers = pyupbit.get_tickers(fiat="KRW")
            max_count = max_count + 1
            
            ticker_list.append(tickers[max_count][4:])
            time.sleep(0.05)
            
            if max_count >= len(tickers)-1:
                break

    except Exception:
        raise

    return ticker_list

# processing time = 20 sec
# return coin ticker
def get_filtered_ticker(value):
    get_ticker_price = list()
    max_count = -1
    dic = dict()
    try:
        while True:
            max_count = max_count + 1

            # get coin tickers and coin current value
            tickers = get_all_ticker()
            get_ticker_price.append(pyupbit.get_current_price(tickers[max_count]))
            time.sleep(0.05)
            if(1000 < get_ticker_price[max_count] < value):
                dic[str(tickers[max_count])] = get_ticker_price[max_count]

            if max_count >= len(tickers)-1:
                break
               
    except Exception:
        raise
    
    return dic

def get_ticker_price(ticker):
    price = list()
    max_count = 0
    try:
        while True:
            price.append(pyupbit.get_current_price(ticker[max_count]))
            max_count += 1
            time.sleep(0.05)
            if max_count >= len(ticker)-1:
                break

    except Exception:
        raise

    return price

# Get top 10% trading volume
def get_trade_volume():
    ticker_key = list()
    trade_value = list()
    acc_trade_result = dict()
    change_rate = dict()
    headers = {"Accept": "application/json"}
    ticker_key = list(get_filtered_ticker(100000)) # return dictionary
    
    max_count = -1
    loop_count = 0
    try:
        while True:
            max_count = max_count + 1
            loop_count = loop_count + 1
            url = "https://api.upbit.com/v1/ticker?markets=" + ticker_key[max_count]
            response = requests.request("GET", url, headers=headers).json()
            trade_value = json.loads(json.dumps(response, indent=4))
            
            if trade_value[0]['change'] == 'RISE':
                acc_trade_result[trade_value[0]['market']] = round(trade_value[0]['acc_trade_volume_24h'], 8)
                change_rate[trade_value[0]['market']] = round(trade_value[0]['signed_change_rate'], 3)
            
            time.sleep(0.05)    
            if loop_count > len(ticker_key)-1:
                break
    except Exception:
        raise
    
    change_rate = sorted(change_rate.items(), key=operator.itemgetter(1))
    acc_trade_result = sorted(acc_trade_result.items(), key=operator.itemgetter(1))
    return change_rate, acc_trade_result

