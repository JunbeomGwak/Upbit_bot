from urllib import response
import requests
import pandas as pd
import time
import pyupbit
# ref : https://dev-guardy.tistory.com/93?category=860353
# ref : https://coinpipe.tistory.com/162

def rsi(ohlc: pd.DataFrame, period: int = 14):
    ohlc["trade_price"] = ohlc["trade_price"]
    delta = ohlc["trade_price"].diff()
    gains, declines = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    declines[declines > 0] = 0

    _gain = gains.ewm(com=(period - 1 ), min_periods=period).mean()
    _loss = declines.abs().ewm(com=(period - 1), min_periods=period).mean()

    RS = _gain / _loss
    return pd.Series(100 - (100 / (1 + RS)), name="RSI")

def MACD(tradePrice):
    exp12 = tradePrice.ewm(span=12, adjust=False).mean()
    exp26 = tradePrice.ewm(span=26, adjust=False).mean()
    macd = exp12 - exp26
    exp = macd.ewm(span=9, adjust=False).mean()
    return exp

def get_ma(df, n):
    return df['close'].rolling(window=n).mean()

df = pyupbit.get_ohlcv()
ma80 = get_ma(df, 80)
print(ma80)

'''
if __name__ == "__main__":
    while True:
        url = "https://api.upbit.com/v1/candles/minutes/1"
        querystring = {"market":"KRW-JST", "count":"200"}
        response = requests.request("GET", url, params=querystring)

        data = response.json()

        df_macd = pd.DataFrame(data)
        df_rsi = pd.DataFrame(data)

        df_rsi = df_rsi.reindex(index=df_rsi.index[::-1]).reset_index()
        nrsi = rsi(df_rsi, 14).iloc[-1]
        df_macd=df_macd.iloc[::-1]

        macd = MACD(df_macd['trade_price'])

        print(f'현재 macd: {macd[0]}')
        print(f'현재 rsi: {nrsi}')
        time.sleep(1)
'''