# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import datetime
import time

from simple.common.util.properties_util import properties, DB_DATA, STOCK_DATA, \
    CRAWLER
from simple.common.util.time_util import getTodayWithFormatting, \
    getDayFromSpecificDay, convertStringToDatetime, \
    convertStringToTime, getDayFromSpecificDay, getTodayWithFormatting
from simple.data.controlway.crawler import data_crawler
from simple.data.controlway.crawler.data_crawler import PAGE_NUM, \
    getTotalPageNum, getHistoricalData
from simple.data.controlway.dataframe import process_dataframe
from simple.data.controlway.dataframe.process_dataframe import get_stock_data_using_datareader, register_stock_data_in_db, \
                                                                register_stock_data_in_db
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.controlway.db.factory.data_handler_factory import getDataHandler, \
    close
from simple.data.controlway.db.mysql.data_handler import DataHandler
from simple.data.controlway.db.mysql.query import select_query
from simple.data.controlway.db.mysql.query.insert_query import INSERT_STOCK_ITEM_DAILY_01
from simple.data.controlway.db.mysql.query.select_query import SELECT_TARGET_PORTFOLIO
from simple.data.stock import process_stock_data
from simple.data.stock.stock_data import StockColumn, MARKET_OPEN_TIME, \
    MARKET_CLOSE_TIME, stock_data, StockTable


def pre_process():
    
    print "pre_process starting"
    
    # 0. STOCK_RELATED_DATA init
    tempMarketOpenTime = properties.get_selection(STOCK_DATA)[MARKET_OPEN_TIME]
    tempMarketCloseTime = properties.get_selection(STOCK_DATA)[MARKET_CLOSE_TIME]
     
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
    
    '''
    
        1. TARGET_PORTFOLIO 읽어오기
         1.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기 
        2. LIVE_PORTFOLIO 읽어오기
         2.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기
        3. 읽어온 종목 코드들의 최신 YM_DD를 가지고   
    
    ''' 
    
    # 1. TARGET_PORTFOLIO 선처리
    #  1.1 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    data_handler = data_handler_factory.getDataHandler()
    cursor = data_handler.openSql(SELECT_TARGET_PORTFOLIO)
    stock_items = cursor.fetchall()
    
    
    '''
          설계 :TARGET에 있는 STOCK_ITEMS를 뽑아오고
              뽑아온 STOCK_ITEM을 2년이내로 정보를 가져오자. (옵션으로 빼고)
    '''
    
    for stockItem in stock_items:
        print stockItem['STOCK_CD']
        start = getDayFromSpecificDay(time.time(), -700, "%Y%m%d")
        end = getTodayWithFormatting("%Y%m%d")
        pageNum = properties.get_selection(CRAWLER)[PAGE_NUM]
        totalPageNum = data_crawler.getTotalPageNum(stockItem[StockColumn.STOCK_CD],
                                     start, end, pageNum)
        rows = data_crawler.getHistoricalData(stockItem[StockColumn.STOCK_CD],
                                              start, end, int(pageNum), int(totalPageNum))
        data_handler.execSqlManyWithParam(INSERT_STOCK_ITEM_DAILY_01,
                                           rows)
        
        
    data_handler_factory.close(data_handler)
    
    
    
    # 2. LIVE_PORTFOLIO 선처리
    #  2.2 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    
    
if __name__ == '__main__':
    print "simple_biz_preprocess test"
#     pre_process()
    