# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 17.

@author: lee
'''

import datetime
import time
import numpy as np

from zipline.algorithm import TradingAlgorithm
from zipline.api import order, record, symbol, order_target, history, add_history

import pandas_datareader.data as web

import matplotlib.pyplot as plt
import pandas as pd
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getHistoricalData


def initialize(context):
    add_history(5, '1d', 'price')
    add_history(20, '1d', 'price')
    context.i = 0
    context.stockCd = '035720'
    context.investment = False
     
def handle_data(context, data):
#     order(symbol('035720'), 1)

    context.i += 1
    if context.i < 20:
        return

    ma5 = history(5, '1d', 'price').mean()
    ma20 = history(20, '1d', 'price').mean()
    buy = False
    sell = False
    sym = symbol(context.stockCd)
    
    if ma5[sym] > ma20[sym] and context.investment == False:
        order_target(sym, 1)
        context.investment = True
        buy = True
    elif ma5[sym] < ma20[sym] and context.investment == True:
        order_target(sym, -1)
        context.investment = False
        sell = True
    
    record(kakao=data[sym].price, ma5=ma5[sym], ma20=ma20[sym], buy=buy, sell=sell)
    

if __name__ == '__main__':
    
    stockCd = "035720"
    path = "C:/Windows/System32/git/PythonExample/PythonTetEnv/stock_data/"
    
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    
    
    # Write
    '''
    dates = pd.date_range(start, end)
    rows = getHistoricalData(stockCd, start, end)
    
    df = pd.DataFrame(rows, 
                      columns=["Date", "Open", "High", "Low", 
                               "Close", "Volume", "Adj Close"])
    df.set_index(df['Date'], inplace=True)
    df = df.drop('Date', 1)
    df = df[['Close']]
    df.columns = [stockCd]
    df = df.convert_objects(convert_numeric=True)
    df.index = pd.to_datetime(df.index)
    df = df.tz_localize("UTC")
    df.sort_index(inplace=True)
    df.to_csv(path + stockCd + ".csv")
    '''
    
    # Read (DataFrame)

    data = web.DataReader("AAPL", "yahoo", start, end)
    data = data[['Adj Close']]
    data.columns = [stockCd]
    data = data.tz_localize("UTC")
    
    df = pd.read_csv(path + stockCd + ".csv", index_col='Date')
    df.index = pd.to_datetime(df.index)
    df = df.tz_localize("UTC")
    
    data = data[len(data) - len(df):]
    data[stockCd] = np.where(1, df[stockCd], df[stockCd])
    
    
    algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
    results = algo.run(data)

    print results[['starting_cash', 'ending_cash', 'ending_value', 'portfolio_value']]
#     print results.info()
    
    results[['ma5', 'ma20']].plot()
#     results[['portfolio_value']].plot()
    
    plt.plot(results.ix[results.buy == True].index, results.ma5[results.buy == True], '^')
    plt.plot(results.ix[results.sell == True].index, results.ma5[results.sell == True], 'v')
    
    plt.show()
    
    
    '''
    plt.plot(results.index, results.portfolio_value)
    plt.show()
    '''   
