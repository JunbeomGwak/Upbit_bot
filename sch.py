from webbrowser import BackgroundBrowser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from buy_sell_market_price import *
from get_coin_info import *
import time
import os

def runner():
    compare_updown_rate(100000)

def compare_updown_rate(value, buy_amount):
    max_count = -1
    count = 0
    first = get_filtered_ticker(value)
    first_key = list(first.keys())
    first_value = list(first.values())
    time.sleep(1)
    second = get_filtered_ticker(value)
    second_value = list(second.values())
    result = list()

    try:
        while True:
            max_count = max_count + 1
            
            if max_count > len(first)-1:
                break
            elif first_value[max_count]*1.02 > second_value[max_count]:
                result.append(first_key[max_count])
                time.sleep(0.05)
    except Exception:
        raise

    while count < len(result):
        buycoin_market(result[count], buy_amount)

    print(result)


if __name__ == '__main__':
    
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(runner, 'cron', minute=18)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()