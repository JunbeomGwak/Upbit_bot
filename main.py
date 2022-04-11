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
from get_volume_power import *
from get_trade_price import *
rate = dict()
trade = dict()

sched = BackgroundScheduler(timezone='Asia/Seoul')

#@sched.scheduled_job('cron', hour=8, minute=57, id='get_data')
#@sched.scheduled_job('cron', hour=9, minute=30, id='top5bid')
def buy(count):
    market_code = top5bid(count)
    balance = get_my_balance()
    buycoin_market(market_code, balance)

@sched.scheduled_job('interval', seconds=2, id='test1')
def test():
    print("start")
    data = test()
    #data = data.sort()
    for i in range(10):
        print(data[i])
#@sched.scheduled_job('cron', hour=9, minute=15, second=40,id='sell_coin')
def sell():
    count = 1
    while count < len(get_my_coin_balance()):
        coin = str('KRW-' + str(get_my_coin_balance()[count]['currency']))
        count = count + 1
        sellcoin_market(coin)
        if count > len(get_my_coin_balance()):
            break

if __name__ == '__main__':
    #sched.start()
    data = get_trading_volume()
    for i in range(10):
        print(data)
    #sched.add_job(test, 'interval', seconds=30, id="test1")
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()
