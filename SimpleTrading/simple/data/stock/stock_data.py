# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import datetime

from simple.common.util.properties_util import *

class StockTable():
    STOCK_ITEM = "STOCK_ITEM"
    STOCK_ITEM_DAILY = "STOCK_ITEM_DAILY"
    STOCK_TEST = "STOCK_TEST"
    
class StockColumn():
    STOCK_CD = "STOCK_CD"
    MARKET_CD = "MARKET_CD"
    YM_DD = "YM_DD"

class StockData():

    def __init__(self):
        self.dict = {}
        pass
#     def set_market_time(self, open_time, close_time):
#         self.dict[MARKET_OPEN_TIME] = open_time
#         self.dict[MARKET_CLOSE_TIME] = close_time
        
stock_data = StockData() 

if __name__ == '__main__':
  
    '''  
    properties_path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/stock.properties"
    properties = PropertiesUtil(properties_path)

    temp_market_open_time = properties.config_section_map(STOCK_DATA)[MARKET_OPEN_TIME]
    temp_market_close_time = properties.config_section_map(STOCK_DATA)[MARKET_CLOSE_TIME]
    
    time = temp_market_open_time.split(":")
    hour = int(time[0])
    min = int(time[1]) 
    market_open_time = datetime.time(hour, min, 0, 0)
    
    time = temp_market_close_time.split(":")
    hour = int(time[0])
    min = int(time[1]) 
    market_close_time = datetime.time(hour, min, 0, 0)
    
    STATIC_MARKET_OPEN_TIME = market_open_time
    STATIC_MARKET_CLOSE_TIME = market_close_time
    '''