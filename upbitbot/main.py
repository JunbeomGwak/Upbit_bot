import time
from unicodedata import decimal
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError
from import_module import *
from buy_sell_market_price import *
from get_coin_info import *
from get_volume_power import *
from get_trade_price import *
rate = dict()
trade = dict()

sched = BackgroundScheduler(timezone='Asia/Seoul')

@sched.scheduled_job('cron', hour=8, minute=59, id='toptrade_09')
def start():
    print(datetime.now())
    ticker = toptrade()
    print(f'Top trade ticker\n{ticker[:5]}')

@sched.scheduled_job('cron', hour=9, minute=30, id='toptrade_buy')
def buyticker():
    count = 5
    ticker = toptrade()
    divide = get_my_balance/count
    for i in range(0, count):
        rate = get_trade_rate(ticker[i])
        if rate > 0:
            buycoin_market(ticker[i], divide)
            print(f"{datetime.now()}, Buy {ticker[i]}")
            time.sleep(1)
    

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
