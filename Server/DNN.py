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


def Strategy_DNN(df):
    df['returns'] = np.log(df / df.shift(1))
    df.dropna(inplace=True)
    df['direction'] = np.sign(df['returns']).astype(int)

    # create lags
    lags = 2
    global cols
    cols = []
    for lag in range(1, lags + 1):
        col = 'lag_{}'.format(lag)
        df[col] = df['returns'].shift(lag)
        cols.append(col)
    df.dropna(inplace=True)

    global cols_bin
    cols_bin = []
    for col in cols:
        col_bin = col + '_bin'
        df[col_bin] = np.digitize(df[col], bins=[0])
        cols_bin.append(col_bin)

    model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=2 * [250], random_state=1)
    model.fit(df[cols_bin], df['direction'])

    df['pos_dnn_sk'] = model.predict(df[cols_bin])
    df['strat_dnn_sk'] = df['pos_dnn_sk'] * df['returns']

    stats = df[['returns', 'strat_dnn_sk']].cumsum().apply(np.exp).calc_stats()
    return stats

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", help="stock")
args = argParser.parse_args()

df = get_closed_price('aapl', '2020-01-01', '2023-02-11')

quantResult = Strategy_DNN(df)


print(quantResult.stats.to_json())