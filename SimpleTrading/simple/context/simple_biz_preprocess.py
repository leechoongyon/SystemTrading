# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import datetime
import time

from simple.common.util.properties_util import properties, STOCK_DATA, \
    MARKET_OPEN_TIME, MARKET_CLOSE_TIME
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.insert_query import INSERT_TARGET_PORTFOLIO_01
from simple.data.stock.stock_data import stock_data
from simple.portfolio import target_portfolio


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
    
    init()
    
    dataHandler = data_handler_factory.getDataHandler()
    
    recommend = target_portfolio.selectionOfStockItems()
    
    print recommend
#     dataHandler.execSqlManyWithParam(INSERT_TARGET_PORTFOLIO_01, rows)
    data_handler_factory.close(dataHandler)
    
    
if __name__ == '__main__':
    print "simple_biz_preprocess test"
#     pre_process()
    