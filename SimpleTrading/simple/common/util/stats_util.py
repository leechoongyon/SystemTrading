# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 4.

@author: lee
'''


import math
import os
import time

import numpy as np
import pandas as pd
from simple.common.util.plt_util import plotData
from simple.common.util.properties_util import properties, STOCK_DATA, \
    STOCK_DOWNLOAD_PATH
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
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

# 수익률 구하기 로그 형태로
# 아마추어 퀀트에서 설명한 로그 수익률 구하기 (이게 정확)
# 로그 수익률 = ln(오늘 가격 / 어제 가격) = ln(오늘가격) - ln(어제가격)
def getLogEarningsRate(df):
    return np.log(df[1:] / df[:-1].values) 

# 수익률 구하기 (이게 실제)
def getEarningsRate(df):
    earningsRate = df['Close'].copy()
    earningsRate[1:] = (earningsRate[1:] / earningsRate[:-1].values) - 1
    earningsRate[0] = 0
    return earningsRate

def getLog(df):
    return np.log(df).round(2)

# log_spread와 log_spread_residual 는 다르다. residual는 잔차다 (두 개간의 차이)
# 로그스프레드와 로그수익률은 다른 개념
def getLogSpread(df, cointegration, symbols):
    lnDf = getLog(df)
    logSpread = lnDf[symbols[0]] - cointegration * lnDf[symbols[1]]
    return logSpread

def getLogSpreadResidual(df, cointegration, symbols):
    logSpread = getLogSpread(df, cointegration, symbols) 
    logSpreadMean = logSpread.mean()
    logSpreadResidual = logSpread - logSpreadMean
    return logSpreadResidual

# 이건 로그 이용해서 cointegration 구하기 (아마추어 퀀트)
def getCointegrationUsingLog(df, symbols):
    lnDf = np.log(df).round(2)
    cointegration = lnDf.cov()[symbols[0]][symbols[1]] / lnDf[symbols[1]].var()
    return cointegration

# 로그 이용해서 상관계수 구하기
def getCorrelationCoefficientUsingLog(df, symbols):
    # A와 B의 공분산 / (A의 로그 표준편차 * B의 로그 표준편차)
    cointegration = getCointegrationUsingLog(df, symbols)
    correlationCofficient = cointegration / ( df[symbols[0]].values.std() * df[symbols[1]].values.std() )
    return correlationCofficient

# -----------------------------------------------------

# 이건 수익률을 이용해서 각 공분산을 구한 뒤 cointegration 구하기
def getCointegrationUsingearningsRate(df, symbols):
    pass

if __name__ == '__main__':
    
    # 한 종목의 로그수익률 그려보기
    # 
    
    startNum = -30
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]

    symbols = ["CJ_CGV", "CJ"]
    dates = pd.date_range(start, end)
    sourceDf = pd.read_csv(path + "/" + symbols[0] + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    sourceDf[['Close']] = sourceDf[['Close']].apply(pd.to_numeric)
    refinedDf = np.log(sourceDf[1:] / sourceDf[:-1].values)
    plotData(refinedDf)
    
    '''
    
    startNum = -30
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    
    symbols = ["CJ_CGV", "CJ"]
    dates = pd.date_range(start, end)
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]
    
    df = pd.DataFrame(index=dates)
    sourceDf = pd.read_csv(path + "/" + symbols[0] + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    targetDf = pd.read_csv(path + "/" + symbols[1] + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    df_temp = sourceDf.rename(columns={'Close': symbols[0]})
    df = df.join(df_temp)
    df_temp = targetDf.rename(columns={'Close': symbols[1]})
    df = df.join(df_temp)
    
    refinedDf = df.dropna()
    
    print getCointegrationUsingLog(refinedDf, symbols)
    print getCorrelationCoefficientUsingLog(refinedDf, symbols)
    '''