'''
Created on 2016. 8. 9.

@author: lee
'''
import time

from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DATA, STOCK_DOWNLOAD_PATH, TARGET_PORTFOLIO, \
    TOIN_CODES
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getIntradayData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_TARGET_PORTFOLIO, \
    SELECT_STOCK_ITEM_WITH_PARAM


def buy():
    dataHandler = data_handler_factory.getDataHandler()
    cursor = dataHandler.openSql(SELECT_TARGET_PORTFOLIO)
    results = cursor.fetchall()
    items = []
    for result in results:
        items.append(result)
    
    # 하루치 현재가 가져오기
    for item in items:
        getIntradayData(item['STOCK_CD'])
    

    data_handler_factory.close(dataHandler)

def sell():
    pass

def recommend():
    # 0. 초기세팅
    dataHandler = data_handler_factory.getDataHandler()
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]


    # 1. 업종별 테이블 조회
    # 일단 테스트를 위해 properties 정의된 업종만 조회     
    raws = properties.getSelection(TARGET_PORTFOLIO)[TOIN_CODES].split(",")
    toinCodes = []
    for raw in raws:     
        toinCodes.append(raw)
    
    for toinCode in toinCodes:
        dataHandler = data_handler_factory.getDataHandler()
        cursor = dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_PARAM, 
                                              toinCode)
        stockItems = cursor.fetchall()
        
        # techAnalysis 
        # 여기서 pair 종목을 전부 뽑아냄.
        # 리턴 컬럼 sourcePair, targetPair, cointegration, residual, correlationCoefficient
        techResult = techAnalysis(stockItems)
        
    
    data_handler_factory.close(dataHandler)
    
def valueAnalysis():
    pass

def techAnalysis():
    pass
