# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
from simple.data.controlway.crawler.data_crawler import getIntradayData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_LIVE_PORTFOLIO


def pre_process():
    pass    

def post_process():
    pass

def perform():
    
    pre_process()
    
    '''
        1. LIVE_PORTFOLIO
         1.1 LIVE_PORTFOLIO 에서 주식종목 가져옴
          1.1.1 가져온 종목에 대해서 페어트레이딩 실시
          1.1.2 볼린저 밴드 적용
    '''

    dataHandler = data_handler_factory.getDataHandler()
    cursor = dataHandler.openSql(SELECT_LIVE_PORTFOLIO)
    results = cursor.fetchall()
    items = []
    for result in results:
        items.append(result)
    
    # 하루치 현재가 가져오기
    for item in items:
        getIntradayData(item['STOCK_CD'])
    

    data_handler_factory.close(dataHandler)  

    post_process()