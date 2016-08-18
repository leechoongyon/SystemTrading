# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 17.

@author: lee
'''

import datetime
import time
import matplotlib.pyplot as plt

from zipline.algorithm import TradingAlgorithm
from zipline.api import order, record, symbol
import pandas as pd
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getHistoricalData

 
def initialize(context):
    pass

     
def handle_data(context, data):
    order(symbol('035720'), 1)

if __name__ == '__main__':
    
    stockCd = "035720"
    path = "C:/Windows/System32/git/PythonExample/PythonTetEnv/stock_data/"
    
    # Write
    '''
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    
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
    df = pd.read_csv(path + stockCd + ".csv", index_col='Date')
    df.index = pd.to_datetime(df.index)
    df = df.tz_localize("UTC")
    print df
    
    algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
    results = algo.run(df)
    print results[['starting_cash', 'ending_cash', 'ending_value']].head()
    
    
    '''
    plt.plot(results.index, results.portfolio_value)
    plt.show()
    '''   
