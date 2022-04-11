# -*- coding: utf-8 -*-
from locale import currency
import requests
from get_coin_info import get_my_balance

currency_code = "KRW"
count = 5
bid_url = f"https://crix-api-cdn.upbit.com/v1/crix/trends/daily_volume_power?quoteCurrencyCode={currency_code}&orderBy=bid&count={count}"
ask_url = f"https://crix-api-cdn.upbit.com/v1/crix/trends/daily_volume_power?quoteCurrencyCode={currency_code}&orderBy=ask&count={count}"

bid_response = requests.get(bid_url).json()
ask_response = requests.get(ask_url).json()

def top5bid(count):
    for i in range(0, count):
        market_code = bid_response["markets"][i]["pair"]
        change_price = bid_response["markets"][i]["signedChangePrice"]
        change_rate = round(bid_response["markets"][i]["signedChangeRate"],2)

        print(f"Coin name: {market_code}\tChange_price: {change_price}\tChange_rate: {change_rate}")
    
    return market_code, change_price, change_rate

def top5ask(count):
    for i in range(0, count):
        market_code = ask_response["markets"][i]["pair"]
        change_price = ask_response["markets"][i]["signedChangePrice"]
        change_rate = round(ask_response["markets"][i]["signedChangeRate"],2)
        print(f"Coin name: {market_code}\tChange_price: {change_price}\tChange_rate: {change_rate}")

    return market_code, change_price, change_rate