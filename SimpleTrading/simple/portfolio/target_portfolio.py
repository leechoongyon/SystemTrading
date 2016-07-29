# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
import time

from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getHistoricalData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_STOCK_ITEM_WITH_PARAM


def pre_process():
    pass

def post_process():
    pass

def perform():

    pre_process()
    
    '''
        1. TARGET_PORTFOLIO 
         1.1 기본적 분석 + 기술적 분석을 통해 종목 추천
         1.2 추천된 종목을 언제 살지 매수 타이밍을 알아본다.
    '''
    
    post_process()
    
    
    
def selectionOfStockItems():
    
    # 1. 업종별 테이블 조회
        
    # 2. 업종별 코드 테이블에서 업종을 받아와서 STOCK_ITEM 조회
        
    toinItems = ["통신업"]
    
    # 3. 업종별 코드 테이블에서 업종을 받아와서 STOCK_ITEM 조회

    dataHandler = data_handler_factory.getDataHandler()
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    for toinItem in toinItems:
        dataHandler = data_handler_factory.getDataHandler()
        cursor = dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_PARAM, "기계")
        stockItems = cursor.fetchall()
        
    # 4. STOCK_ITEM에 해당되는 것을 2년치~3년치 받아옴. (기존 만들어진 것)
    # 이걸 어디다 저장해야하지? 파일이 그나마 제일 나은데 (DataFrame으로 각 종목별로 고가, 저가, 표준편차 등을 Concat시키는거지.)
    #  4.1 DataFrame의 Index를 미리 만들기. (StockCd, High, Low, Adv, Var)
    #  4.2 각각의 rows들을 계산해서 DataFrame에 concat 시키기.    
        
        for stockItem in stockItems:
            rows = getHistoricalData(stockItem['STOCK_CD'], start, end)
            for row in rows:
                print row

    
    
if __name__ == '__main__':
    selectionOfStockItems()    