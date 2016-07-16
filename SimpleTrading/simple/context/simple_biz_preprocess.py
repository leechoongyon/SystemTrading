# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import datetime

from simple.common.util.properties_util import properties, DB_DATA, STOCK_DATA
from simple.common.util.time_util import get_today_with_formatting, \
    get_day_from_specific_day, convert_string_to_datetime, \
    convert_string_to_time
from simple.data.controlway.dataframe.process_stock_data import get_stock_data_using_datareader, \
    register_stock_data_in_db, process_stock_data
from simple.data.controlway.db.factory.data_handler_factory import get_data_handler_in_mysql, \
    close_handler
from simple.data.controlway.db.mysql.data_handler import DataHandler
from simple.data.controlway.db.mysql.query import select_query
from simple.data.stock.stock_data import StockColumn, MARKET_OPEN_TIME, \
    MARKET_CLOSE_TIME, stock_data, StockTable


def pre_process(properties_path):
    
    print "pre_process starting"
    
    # 0. STOCK_RELATED_DATA init
    temp_market_open_time = properties.get_selection(STOCK_DATA)[MARKET_OPEN_TIME]
    temp_market_close_time = properties.get_selection(STOCK_DATA)[MARKET_CLOSE_TIME]
     
    time = temp_market_open_time.split(":")
    hour = int(time[0])
    min = int(time[1]) 
    market_open_time = datetime.time(hour, min, 0, 0)
     
    time = temp_market_close_time.split(":")
    hour = int(time[0])
    min = int(time[1]) 
    market_close_time = datetime.time(hour, min, 0, 0)
     
    stock_data.dict[MARKET_OPEN_TIME] = market_open_time 
    stock_data.dict[MARKET_CLOSE_TIME] = market_close_time
    
    '''
    
        1. TARGET_PORTFOLIO 읽어오기
         1.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기 
        2. LIVE_PORTFOLIO 읽어오기
         2.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기
        3. 읽어온 종목 코드들의 최신 YM_DD를 가지고   
    
    ''' 
    
    # 1. TARGET_PORTFOLIO 선처리
    #  1.1 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    data_handler = get_data_handler_in_mysql()
    cursor = data_handler.openSql(select_query.SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO)
    stock_items = cursor.fetchall()
    
    for stock_item in stock_items:
        ym_dd = stock_item[StockColumn.YM_DD]
        start = get_day_from_specific_day(convert_string_to_time(ym_dd, "%Y%m%d"), +1, "%Y%m%d")
        end = get_today_with_formatting("%Y%m%d")
        stock_cd = stock_item[StockColumn.STOCK_CD]
        market_cd = stock_item[StockColumn.MARKET_CD]
        df = get_stock_data_using_datareader(stock_cd, market_cd, start, end)
        df = process_stock_data(df, stock_cd)
        exists_option = properties.get_selection(DB_DATA)['exists_option']
        db_type = properties.get_selection(DB_DATA)['db_type']
        register_stock_data_in_db(data_handler.get_conn(), df, StockTable.STOCK_ITEM_DAILY, exists_option, db_type) 
        
    close_handler(data_handler)
    
    
    
    # 2. LIVE_PORTFOLIO 선처리
    #  2.2 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    
    
if __name__ == '__main__':
    print "simple_biz_preprocess test"
#     pre_process()
    