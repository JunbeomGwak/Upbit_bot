import sys
import logging
import traceback
import time
import math
import datetime
from unicodedata import decimal
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError
from import_module import *
from buy_sell_market_price import *
from get_coin_info import *
from sch import *

rate = dict()
trade = dict()
def get_trade_volume(value):
    acc_trade_result = dict()
    change_rate = dict()
    
    ticker_name, ticker_price = get_filtered_ticker(value) # return dictionary
    
    url = "https://api.upbit.com/v1/ticker?markets=" + ticker_name[max_count]
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers).json()    
    trade_value = json.loads(json.dumps(response, indent=4))
    
    max_count = 0
    loop_count = 0
    try:
        while True:
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

def runner():
    global rate, trade
    print(f'\n\nStart time: {datetime.now()}')
    rate, trade = get_trade_volume(100000)
    print('Top 5 change rate')
    for i in range(0, 5):
        print(f" {rate[i]}", end="")

    print("\n\nTop 5 trade_volume")
    for i in range(0, 5):
        print(f" {trade[i]}", end="")
    
    print(f'\nEnd time: {datetime.now()}')

runner()