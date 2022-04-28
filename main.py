import time
import pandas
from scheduler import Scheduler
import schedule
import time
from unicodedata import decimal
from datetime import datetime
#from apscheduler.schedulers.background import BackgroundScheduler
#from apscheduler.schedulers.background import BlockingScheduler
#from apscheduler.jobstores.base import JobLookupError
from import_module import *
from buy_sell_market_price import *
from get_coin_info import *
from get_volume_power import *
from get_trade_price import *
from rsi_macd_ma import *
rate = dict()
trade = dict()

def gettop5tickerdata():
    # return top 5 ticker
    toprate = toptrade()
    print(toprate)

def interval():
    rsi, macd = getmacdrsi("KRW-SBD")
    ma = get_ma('KRW-SBD', 80)
    print(f'RSI: {rsi}\tMACD: {macd}\tMA: {ma}')
    return rsi, macd, ma

schedule.every(1).seconds.do(interval)
#schedule.every(1).minute.do(interval)
def process():
    '''
    while True:
        if(current_price > ma):
            if rsi > 30 and rsi < 70:
                print("buy!")
            else:
                continue
        elif (current_price < ma):
            continue
    '''
while True:
    schedule.run_pending()


'''
    sched.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            tim.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sched.shutdown()
'''