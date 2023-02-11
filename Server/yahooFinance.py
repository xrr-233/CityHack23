import yfinance as yf
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-i", help="interval")
args = argParser.parse_args()


def get_closed_price(sign, start_date, end_date):
    stock = yf.Ticker(sign)
    df = stock.history(start = start_date, end = end_date, interval=args.i)
    df = df[['Close']]
    return df

d = get_closed_price("aapl", "2023-02-02", "2023-02-03")
print(d.to_string())