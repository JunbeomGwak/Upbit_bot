import sys
import logging
import traceback
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError
from import_module import *
from buy_market import *
from get_coin_info import *
from sch import *


sched = BackgroundScheduler(timezone='Asia/Seoul')
sched.start()

def runner():
    change_rate = dict()
    acc_trade_volume = dict()
    change_rate, acc_trade_volume = get_trade_volume()
    print('Trade_volume')
    print(change_rate)
    print('\nChange rate')
    print(acc_trade_volume)

if __name__ == '__main__':
    
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(runner, 'cron', minute=6)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()