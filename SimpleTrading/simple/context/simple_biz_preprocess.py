# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

from simple.data.controlway.db.db_data import db_data
from simple.data.controlway.db.mysql.data_handler import DataHandler
from simple.data.controlway.db.query import select_query


def pre_process(properties_path):
    
    print "pre_process starting"
    
    
    
    
    '''
    
        1. TARGET_PORTFOLIO 읽어오기
         1.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기 
        2. LIVE_PORTFOLIO 읽어오기
         2.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기
        3. 읽어온 종목 코드들의 최신 YM_DD를 가지고   
    
    ''' 
    
    # 1. TARGET_PORTFOLIO 선처리
    #  1.1 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    data_handler = DataHandler(db_data.host, db_data.user, db_data.passwd, db_data.db,\
                               db_data.charset, db_data.use_unicode)
    
    
    cursor = data_handler.openSql(select_query.SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO)
    results = cursor.fetchall()
    target_stock_item = []
    for result in results:
        target_stock_item.append(result)
        print result[0]
    
        
    
    data_handler.close()
    
    
    
    # 2. LIVE_PORTFOLIO 선처리
    #  2.2 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    
    
if __name__ == '__main__':
    pre_process()