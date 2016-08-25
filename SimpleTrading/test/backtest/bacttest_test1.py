'''
Created on 2016. 8. 24.

@author: lee
'''

import time

import pandas as pd
from simple.common.util import file_util
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DATA, STOCK_DOWNLOAD_PATH
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getHistoricalData

from zipline.algorithm import TradingAlgorithm
from zipline.api import order, record, symbol, order_target, history, add_history

def initialize(context):
    pass

def handle_data(context, data):
    print data

if __name__ == '__main__':
    stockCd = "035720"
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH] + "/" + end + "/"
    stockFilePath = path + "/" + stockCd + ".csv"
    
    # Write
    if not file_util.isFile(stockFilePath):
        file_util.mkdir(path)
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
    
    
    df = pd.read_csv(path + stockCd + ".csv", index_col='Date')
    df.index = pd.to_datetime(df.index)
    df = df.tz_localize("UTC")
        
    algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
    results = algo.run(df)
    
