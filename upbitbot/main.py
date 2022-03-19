import sys
import logging
import traceback
import time
import datetime

from import_module import *
from buy_market import *
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError

if __name__ == '__main__':
    sched = BackgroundScheduler(timezone='Asia/Seoul')
    sched.start()
    '''
    count = 0
    while True:
        #logging.info('Running scheduled job...')
        #sched.add_job(buycoin_market, "cron", minute="42", second="01", id="test_1", args=['KRW-CELO', '6000'])
        #sched.add_job(sellcoin_market, "cron", minute="42", second="30", id="test_2", args=['KRW-CELO'])
        #time.sleep(1)
        #sched.remove_all_jobs()
    '''
    #buycoin_market('KRW-STRK', '10000')
    #get_balance('KRW-STRK')
    #sellcoin_market('KRW-STRK')