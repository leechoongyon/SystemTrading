# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 10.

@author: lee
'''
 
import math
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from simple.common.util.properties_util import properties, STOCK_DATA
from simple.config.configuration import PROPERTIES_PATH


def symbolToPath(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def getData(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbolToPath(symbol, properties.getSelection(STOCK_DATA)['stock_download_path']), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    return df

def getCloseData(symbols, dates):
    """Read stock data (close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbolToPath(symbol, properties.getSelection(STOCK_DATA)['stock_download_path']), index_col='Date',
                parse_dates=True, usecols=['Date', 'Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Close': symbol})
        df = df.join(df_temp)

    return df


def plotData(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def normalizePrice(df):
    pass
    
def computeDailyReturns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    daily_returns = df.copy()
    
    # 1일 앞부터 시작해서 뒤에서 -1까지 해야 수가 같겠지
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    # Note: Returned DataFrame must have the same number of rows
    return daily_returns

def normalize(symbols, dates, df):
    
    # Compute mean, std
    means = {}
    stds = {}
    for symbol in symbols:
        means[symbol] = df[symbol].mean()
        stds[symbol] = df[symbol].std()
        
    # normalize
    normal_df = pd.DataFrame(index=dates)
    
    for symbol in symbols:
        df_temp = (df[symbol] - means[symbol]) / stds[symbol]
        normal_df = normal_df.join(df_temp)
        
    return normal_df


# symbols required argument 2
# 사용법 : symbols 2개가 넘어오고 정규화된 dataFrame이 넘어오면 그것의 values subtract
# 해서 normalize_spread를 만듬
def normalizeSpread(symbols, normal_df):
    df_list = []
    for symbol in symbols:
        df_list.append(normal_df[symbol])
    
    normal_spread_df = pd.DataFrame(df_list[0].values - df_list[1].values, index=normal_df.index)
    return normal_spread_df

# 수익률 구하기
def getEarningsRate(after_stock_price, before_stock_price):
    return math.log(after_stock_price / before_stock_price)


def getLog(df):
    return np.log(df).round(2)

# log_spread와 log_spread_residual 는 다르다. residual는 잔차다 (두 개간의 차이)
def getLogSpread(df, cointegration, symbols):
    ln_df = getLog(df)
    log_spread = ln_df[symbols[0]] - cointegration * ln_df[symbols[1]]
    return log_spread

def getLogSpreadResidual(df, cointegration, symbols):
    log_spread = getLogSpread(df, cointegration, symbols) 
    log_spread_mean = log_spread.mean()
    log_spread_residual = log_spread - log_spread_mean
    return log_spread_residual

def getCointegration(df, symbols):
    ln_df = np.log(df).round(2)
    cointegration = ln_df.cov()[symbols[0]][symbols[1]] / ln_df[symbols[1]].var()
    return cointegration