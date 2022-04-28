import time
#from scheduler import Scheduler
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
rate = dict()
trade = dict()

def getdata():
    toprate  = toptrade()
    
'''
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
'''