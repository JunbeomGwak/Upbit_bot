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


#sched = BackgroundScheduler(timezone='Asia/Seoul')
#sched.start()

def runner():
    print(f'\n\nStart time: {datetime.now()}')
    rate, trade = get_trade_volume(100000)
    print('Top 5 change rate')
    for i in range(0, 5):
        print(f" {rate[i]}", end="")

    print("\n\nTop 5 trade_volume")
    for i in range(0, 5):
        print(f" {trade[i]}", end="")
    
    print(f'\nEnd time: {datetime.now()}')
if __name__ == '__main__':
    runner()
    '''
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    #scheduler.add_job(runner, 'cron', minute=6)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    '''
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
