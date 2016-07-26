# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import datetime
import time

from simple.common.util.properties_util import properties, DB_DATA, STOCK_DATA, \
    CRAWLER, BIZ_PRE_PROCESS, MARKET_OPEN_TIME, MARKET_CLOSE_TIME, \
    TARGET_DATA_LOAD, LIVE_DATA_LOAD, TARGET_DATA_LOAD_PERIOD
from simple.common.util.time_util import getTodayWithFormatting, \
    getDayFromSpecificDay, convertStringToDatetime, \
    convertStringToTime, getDayFromSpecificDay, getTodayWithFormatting
from simple.data.controlway.crawler import data_crawler
from simple.data.controlway.crawler.data_crawler import PAGE_NUM, \
    getTotalPageNum, getHistoricalData 
from simple.data.controlway.dataframe import process_dataframe
from simple.data.controlway.dataframe.process_dataframe import getStockDataUsingDatareader, registerStockDataInDb, \
                                                                registerStockDataInDb
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.controlway.db.factory.data_handler_factory import getDataHandler, \
    close
from simple.data.controlway.db.mysql.data_handler import DataHandler
from simple.data.stock import process_stock_data
from simple.data.stock.process_stock_data import getTargetPortfolio, \
    insertTargetPortfolioStockData, \
    getLivePortfolio, insertLivePortfolioStockData
from simple.data.stock.stock_data import StockColumn, \
    stock_data, StockTable


def init():
    tempMarketOpenTime = properties.getSelection(STOCK_DATA)[MARKET_OPEN_TIME]
    tempMarketCloseTime = properties.getSelection(STOCK_DATA)[MARKET_CLOSE_TIME]
    
    marketTime = tempMarketOpenTime.split(":")
    hour = int(marketTime[0])
    min = int(marketTime[1]) 
    marketOpenTime = datetime.time(hour, min, 0, 0)
     
    marketTime = tempMarketCloseTime.split(":")
    hour = int(marketTime[0])
    min = int(marketTime[1]) 
    marketCloseTime = datetime.time(hour, min, 0, 0)
     
    stock_data.dict[MARKET_OPEN_TIME] = marketOpenTime 
    stock_data.dict[MARKET_CLOSE_TIME] = marketCloseTime

def preProcess():
    
    print "preProcess starting"
    
    # 0. STOCK_RELATED_DATA init
    init()
    
    '''
        1. TARGET_PORTFOLIO 읽어오기
         1.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기 
        2. LIVE_PORTFOLIO 읽어오기
         2.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기
        3. 읽어온 종목 코드들의 최신 YM_DD를 가지고   
    ''' 
    
    # 1. TARGET_PORTFOLIO 선처리
    #  1.1 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    isTargetDataLoad = properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD]
    if isTargetDataLoad:
        print "executing target data load"
        dataHandler = data_handler_factory.getDataHandler()
        stockItems = getTargetPortfolio(dataHandler)
        startNum = properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD]
        insertTargetPortfolioStockData(stockItems, dataHandler, startNum)
        data_handler_factory.close(dataHandler)
            
    
    # 2. LIVE_PORTFOLIO 선처리
    #  2.2 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    isLiveDataLoad = properties.getSelection(BIZ_PRE_PROCESS)[LIVE_DATA_LOAD]
    if isLiveDataLoad:
        print "executing live data load"
        dataHandler = data_handler_factory.getDataHandler()
        stockItems = getLivePortfolio(dataHandler)
        insertLivePortfolioStockData(stockItems, dataHandler)
        data_handler_factory.close(dataHandler)
        
        
if __name__ == '__main__':
    print "simple_biz_preprocess test"
#     pre_process()
    