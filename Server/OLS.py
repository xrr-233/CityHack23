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


def Strategy_linearOLS_regression(df):
    df['returns'] = np.log(df / df.shift(1))
    df.dropna(inplace=True)
    df['direction'] = np.sign(df['returns']).astype(int)

    lags = 2

    global cols
    cols = []
    for lag in range(1, lags + 1):
        col = 'lag_{}'.format(lag)
        df[col] = df['returns'].shift(lag)
        cols.append(col)
    df.dropna(inplace=True)
    

    model = LinearRegression()
    df['pos_ols_1'] = model.fit(df[cols],df['returns']).predict(df[cols])
    df['pos_ols_2'] = model.fit(df[cols],df['direction']).predict(df[cols])
    df[['pos_ols_1', 'pos_ols_2']].head()
    df[['pos_ols_1', 'pos_ols_2']] = np.where(df[['pos_ols_1', 'pos_ols_2']] > 0, 1, -1)

    df['strat_ols_1'] = df['pos_ols_1'] * df['returns']
    df['strat_ols_2'] = df['pos_ols_2'] * df['returns']
    df[['returns', 'strat_ols_1', 'strat_ols_2']].sum().apply(np.exp)
    straregyMaxReturn = df.cumsum()[['returns', 'strat_ols_1', 'strat_ols_2']].iloc[-1].idxmax()
    
    #get stat
    stats = df[['returns',straregyMaxReturn]].cumsum().apply(np.exp).calc_stats()
    return stats
    
argParser = argparse.ArgumentParser()
argParser.add_argument("-s", help="stock")
args = argParser.parse_args()

df = get_closed_price('aapl', '2020-01-01', '2023-02-11')

quantResult = Strategy_linearOLS_regression(df)


print(quantResult.stats.to_json())