# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 9.

@author: lee
'''
import time

import pandas as pd
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DATA, STOCK_DOWNLOAD_PATH, TARGET_PORTFOLIO, \
    TOIN_CODES
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getIntradayData, \
    getHistoricalData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_TARGET_PORTFOLIO, \
    SELECT_STOCK_ITEM_WITH_PARAM
from simple.data.stock.stock_data import StockColumn
from simple.strategy.pairtrading.common.pair_trading_common import applyPairTrading


class PairTrading():
    
    def __init__(self, start, end, path, dataHandler):
        self.start = start
        self.end = end
        self.path = path
        self.dataHandler = dataHandler
        
    def buy(self):
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
    
    def sell(self):
        pass

    def recommend(self):
        # 1. 업종별 테이블 조회
        # 일단 테스트를 위해 properties 정의된 업종만 조회     
        raws = properties.getSelection(TARGET_PORTFOLIO)[TOIN_CODES].split(",")
        toinCodes = []
        for raw in raws:     
            toinCodes.append(raw)
        
        for toinCode in toinCodes:
            cursor = self.dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_PARAM, 
                                                  toinCode)
            stockItems = cursor.fetchall()
            
            # 2.1 받아온 종목들을 file 에 저장 (DB에 저장하면 리소스 소모 심함)
            for stockItem in stockItems:
                rows = getHistoricalData(stockItem[StockColumn.STOCK_CD], start, end)
                df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                         "Close", "Volume", "Adj Close"])
                df.to_csv(path + "/" + stockItem[StockColumn.STOCK_CD] + ".csv", index=False)
            
            # techAnalysis 
            # 여기서 pair 종목을 전부 뽑아냄.
            # 리턴 컬럼 sourcePair, targetPair, cointegration, residual, correlationCoefficient
            techResults = self.techAnalysis(stockItems)
            print techResults
        
    def valueAnalysis(self):
        pass
    
    def techAnalysis(self, stockItems):
        
        statiList = []
        
        for stockItem in stockItems:
            for pairItem in stockItems:
                stockCd = str(stockItem[StockColumn.STOCK_CD])
                pairCd = str(pairItem[StockColumn.STOCK_CD])
                if (stockCd != pairCd):
                    stati = applyPairTrading(stockCd,
                                            pairCd,
                                            self.start, 
                                            self.end, 
                                            self.path)
                    
                    if (0.5 < stati[2] and stati[2] < 1.5):
                        statiList.append(stati)
                        
        return statiList

if __name__ == '__main__':
    dataHandler = data_handler_factory.getDataHandler()
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]
    pairTrading = PairTrading(start, end, path, dataHandler)
    statiList = pairTrading.recommend()
    
    print type(statiList)
    print statiList