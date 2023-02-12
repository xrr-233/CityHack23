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

# In[124]:


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
    df['PnL'] = df['Strategy'].cumsum().apply(np.exp)
    
    # get stat
    print('SMA stat:' + "\nThe Best Parameters: Short term:", SMA1, " Long term:", SMA2
         ,"\n-------------------------------------------------------------------------")
    stats = df['PnL'].calc_stats()
    return stats



# ### Strategy_linearOLS_regression

# In[119]:


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
    stats = df[straregyMaxReturn].cumsum().apply(np.exp).calc_stats()
    return stats
    



# ### Strategy_NaiveB_LogisticR_SVM

# In[113]:


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
    stats = df[sel][straregyMaxReturn].cumsum().apply(np.exp).calc_stats()
    return stats



# ### Strategy_DNN

# In[115]:


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

    stats = df['strat_dnn_sk'].cumsum().apply(np.exp).calc_stats()
    return stats

df = get_closed_price('aapl', '2022-02-02', '2023-02-03')


quantResult = Strategy_DNN(df)


print(quantResult.stats.to_json())
