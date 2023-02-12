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



# ### Strategy_NaiveB_LogisticR_SVM
# based on 5 digital characteristics, apply NB, LR, SVM, evaluate and find the best model

def Strategy_NaiveBayes_LogisticRression_SVM(df):

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

    mu = df['returns'].mean()
    v = df['returns'].std()
    bins = [mu - v, mu, mu + v]
    global cols_bin
    cols_bin = []
    for col in cols:
        col_bin = col + '_bin'
        df[col_bin] = np.digitize(df[col], bins=bins)
        cols_bin.append(col_bin)

    C = 1
    models = {
        'log_reg': linear_model.LogisticRegression(C=C),
        'gauss_nb': GaussianNB(),
        'svm': SVC(C=C)
        }

    #fit model
    mfit = {model: models[model].fit(df[cols_bin], df['direction'])
        for model in models.keys()}

    #derive_positions
    for model in models.keys():
        df['pos_' + model] = models[model].predict(df[cols_bin])

    #evaluate_strats
    global sel
    sel = []
    for model in models.keys():
        col = 'strat_' + model
        df[col] = df['pos_' + model] * df['returns']
        sel.append(col)
    sel.insert(0, 'returns')
    
    #get stat
    straregyMaxReturn = df[sel].cumsum().iloc[-1].idxmax() 
    stats = df[sel][['returns',straregyMaxReturn]].cumsum().apply(np.exp).calc_stats()
    return stats

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", help="stock")
args = argParser.parse_args()

df = get_closed_price('aapl', '2020-01-01', '2023-02-11')

quantResult = Strategy_NaiveBayes_LogisticRression_SVM(df)


print(quantResult.stats.to_json())