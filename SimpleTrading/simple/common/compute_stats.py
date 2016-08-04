# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 4.

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
        tempDf = pd.read_csv(symbolToPath(symbol, properties.getSelection(STOCK_DATA)['stock_download_path']), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        tempDf = tempDf.rename(columns={'Adj Close': symbol})
        df = df.join(tempDf)

    return df

def getCloseData(symbols, dates):
    """Read stock data (close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        tempDf = pd.read_csv(symbolToPath(symbol, properties.getSelection(STOCK_DATA)['stock_download_path']), index_col='Date',
                parse_dates=True, usecols=['Date', 'Close'], na_values=['nan'])
        tempDf = tempDf.rename(columns={'Close': symbol})
        df = df.join(tempDf)

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
    dailyReturns = df.copy()
    
    # 1일 앞부터 시작해서 뒤에서 -1까지 해야 수가 같겠지
    dailyReturns[1:] = (df[1:] / df[:-1].values) - 1
    dailyReturns.ix[0, :] = 0
    # Note: Returned DataFrame must have the same number of rows
    return dailyReturns

def normalize(symbols, dates, df):
    
    # Compute mean, std
    means = {}
    stds = {}
    for symbol in symbols:
        means[symbol] = df[symbol].mean()
        stds[symbol] = df[symbol].std()
        
    # normalize
    normalDf = pd.DataFrame(index=dates)
    
    for symbol in symbols:
        dfTemp = (df[symbol] - means[symbol]) / stds[symbol]
        normalDf = normalDf.join(dfTemp)
        
    return normalDf


# symbols required argument 2
# 사용법 : symbols 2개가 넘어오고 정규화된 dataFrame이 넘어오면 그것의 values subtract
# 해서 normalize_spread를 만듬
def normalizeSpread(symbols, normalDf):
    dfList = []
    for symbol in symbols:
        dfList.append(normalDf[symbol])
    
    normalSpreadDf = pd.DataFrame(dfList[0].values - dfList[1].values, index=normalDf.index)
    return normalSpreadDf

# 수익률 구하기
def getEarningsRate(afterStockPrice, beforeStockPrice):
    return math.log(afterStockPrice / beforeStockPrice)


def getLog(df):
    return np.log(df).round(2)

# log_spread와 log_spread_residual 는 다르다. residual는 잔차다 (두 개간의 차이)
def getLogSpread(df, cointegration, symbols):
    lnDf = getLog(df)
    logSpread = lnDf[symbols[0]] - cointegration * lnDf[symbols[1]]
    return logSpread

def getLogSpreadResidual(df, cointegration, symbols):
    logSpread = getLogSpread(df, cointegration, symbols) 
    logSpreadMean = logSpread.mean()
    logSpreadResidual = logSpread - logSpreadMean
    return logSpreadResidual

def getCointegration(df, symbols):
    lnDf = np.log(df).round(2)
    cointegration = lnDf.cov()[symbols[0]][symbols[1]] / lnDf[symbols[1]].var()
    return cointegration

