from asyncore import loop
import pyupbit
import time
import requests
import json
import operator

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
    name = get_all_ticker() # all list
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
    
    return ticker_name#, ticker_price

# Get top 10% trading volume
def get_trade_volume(value):
    acc_trade_result = dict()
    change_rate = dict()
    
    ticker_name = get_filtered_ticker(value) # return dictionary
    
    max_count = 0
    loop_count = 0
    try:
        while True:

            url = "https://api.upbit.com/v1/ticker?markets=" + ticker_name[max_count]
            headers = {"Accept": "application/json"}
            response = requests.request("GET", url, headers=headers).json()
        
            trade_value = json.loads(json.dumps(response, indent=4))
            time.sleep(0.2)
            
            if trade_value[0]['change'] == 'RISE':
                acc_trade_result[ticker_name[max_count]] = round(trade_value[0]['acc_trade_volume_24h'], 8)
                change_rate[ticker_name[max_count]] = round(trade_value[0]['signed_change_rate'], 3)
            
            loop_count = loop_count + 1
            max_count = max_count + 1
            if loop_count > len(ticker_name)-1:
                break
    except Exception:
        raise

    change_rate = sorted(change_rate.items(), key=operator.itemgetter(1), reverse=True)
    acc_trade_result = sorted(acc_trade_result.items(), key=operator.itemgetter(1), reverse=True)

    return change_rate, acc_trade_result

'''
test, result = get_trade_volume()
print(test)
print("\n\n")
print(result)
'''