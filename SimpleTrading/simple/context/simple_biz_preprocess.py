# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
from simple.data.controlway.db.mysql.data_handler import DataHandler


def pre_process():
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
    data_handler = DataHandler(host, user, passwd, db, charset, use_unicode)
    
    
    
    
    
    
    
    data_handler.close()
    
    
    
    
    # 2. LIVE_PORTFOLIO 선처리
    #  2.2 PORTFOLIO에 있는 종목 DAILY_DATA 최신화