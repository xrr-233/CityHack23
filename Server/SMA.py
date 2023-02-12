#!/usr/bin/env python
# coding: utf-8

# ### Import Library

# In[94]:


import yfinance as yf
import pandas as pd
import numpy as np
import ffn
import argparse
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from itertools import product
import warnings
warnings.filterwarnings("ignore")


# ### Get Market Data

# In[95]:


def get_closed_price(sign, start_date, end_date):
    stock = yf.Ticker(sign)
    df =  stock.history(start=start_date,  end=end_date)
    df = df[['Close']] # get the close price
    return df


# ### Strategy_SMA

def strategy_SMA(df):
    sma1 = range(20, 60, 5)
    sma2 = range(180, 280, 10)
    results = pd.DataFrame()

    for SMA1, SMA2 in product(sma1, sma2):
        data = pd.DataFrame(df['Close'])
        data.dropna(inplace=True)
        data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))
        data['SMA1'] = data['Close'].rolling(SMA1).mean()
        data['SMA2'] = data['Close'].rolling(SMA2).mean()
        data.dropna(inplace=True)
        data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
        data['Strategy'] = data['Position'].shift(1) * data['Returns']
        data.dropna(inplace=True)
        perf = np.exp(data[['Returns', 'Strategy']].sum())
        results = results.append(pd.DataFrame(
                {'SMA1': SMA1, 'SMA2': SMA2,
                'MARKET': perf['Returns'],
                'STRATEGY': perf['Strategy'],
                'OUT': perf['Strategy'] - perf['Returns']}, # OUT means the difference between market return and strategy return
                index=[0]), ignore_index=True)
    
    results_sort = results.sort_values('OUT', ascending=False)
    
    SMA1 = results_sort['SMA1'].iloc[0]
    SMA2 = results_sort['SMA2'].iloc[0]
    df['SMA_shortTerm'] = df['Close'].rolling(SMA1).mean()
    df['SMA_longTerm'] = df['Close'].rolling(SMA2).mean()
    df.dropna(inplace=True)
    
    # when average price of short term larger than long term, hold long position (indicate by 1)
    # when average price of short term smaller than long term, hold short position (indicate by -1)
    df['Position'] = np.where(df['SMA_shortTerm'] > df['SMA_longTerm'], 1, -1)
    
    df['Returns'] = np.log(df['Close'] / df['Close'].shift(1))
    df['Strategy'] = df['Position'].shift(1) * df['Returns']

    # get stat
    stats = df[['Returns','Strategy']].cumsum().apply(np.exp).calc_stats()
    stats.set_riskfree_rate(.035)
    return stats

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", help="stock")
args = argParser.parse_args()

df = get_closed_price('aapl', '2020-01-01', '2023-02-11')

quantResult = strategy_SMA(df)


print(quantResult.stats.to_json())