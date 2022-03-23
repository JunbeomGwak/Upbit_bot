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

sched = BackgroundScheduler(timezone='Asia/Seoul')

@sched.scheduled_job('cron', hour=8, minute=57, id='get_data')
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

@sched.scheduled_job('cron', hour=9, minute=3, id='buy_coin')
def buy():
    global trade
    balance = get_my_balance()/5
    for i in range(0, 5):
        buycoin_market(trade[i][0], balance)

@sched.scheduled_job('cron', hour=9, minute=15, second=40,id='sell_coin')
def sell():
    count = 1
    while count < len(get_my_coin_balance()):
        coin = str('KRW-' + str(get_my_coin_balance()[count]['currency']))
        count = count + 1
        sellcoin_market(coin)
        if count > len(get_my_coin_balance()):
            break

if __name__ == '__main__':
    sched.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()
