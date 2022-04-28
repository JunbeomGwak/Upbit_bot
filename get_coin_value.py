import pyupbit
import time


def get_all_ticker():
    max_count = -1
    ticker_list = list()
    try:
        while True:
            tickers = pyupbit.get_tickers(fiat="KRW")
            max_count = max_count + 1
            
            ticker_list.append(tickers[max_count][4:])
            time.sleep(0.05)
            
            if max_count >= len(tickers)-1:
                break

    except Exception:
        raise

    return ticker_list


def extract_ticker():
    try:
        test = get_all_ticker()
        print(test)

    except Exception:
        raise

extract_ticker()