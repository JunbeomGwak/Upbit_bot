from urllib import response
import requests
import pandas as pd
import time

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

if __name__ == "__main__":
    while True:
        url = "https://api.upbit.com/v1/candles/minutes/1"
        querystring = {"market":"KRW-JST", "count":"200"}
        response = requests.request("GET", url, params=querystring)

        data = response.json()

        df = pd.DataFrame(data)
        df=df.iloc[::-1]

        macd = MACD(df['trade_price'])
        print(macd[0])
        time.sleep(1)
'''
while True:
    url = "https://api.upbit.com/v1/candles/minutes/1"
    querystring = {"market":"KRW-JST", "count":"200"}
    response = requests.request("GET", url, params=querystring)
    data = response.json()
    df = pd.DataFrame(data)
    df = df.reindex(index=df.index[::-1]).reset_index()
    nrsi = rsi(df, 14).iloc[-1]
    print(f"현재 rsi : {nrsi}")
    time.sleep(1)
'''
