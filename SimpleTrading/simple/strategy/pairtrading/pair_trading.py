# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 9.

@author: lee
'''

import time

import pandas as pd
from simple.common.util import file_util
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DATA, STOCK_DOWNLOAD_PATH, TARGET_PORTFOLIO, \
    TOIN_CODES
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getIntradayData, \
    getHistoricalData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_TARGET_PORTFOLIO, \
     SELECT_STOCK_GROUP, \
    SELECT_STOCK_ITEM_WITH_GROUP_CD, SELECT_STOCK_ITEM_WITH_TOIN_CD
from simple.data.stock.stock_data import StockColumn
from simple.strategy.pairtrading.common.pair_trading_common import PairTradingCommon


class PairTrading():
    
    def __init__(self, start, end, path, dataHandler, types):
        self.start = start
        self.end = end
        self.path = path
        self.dataHandler = dataHandler
        self.types = types
        self.pairTradingCommon = PairTradingCommon(self.start, self.end, self.path)
    
    def __del__(self):
        data_handler_factory.close(self.dataHandler)
        
    def buy(self):
        cursor = dataHandler.openSql(SELECT_TARGET_PORTFOLIO)
        results = cursor.fetchall()
        items = []
        for result in results:
            items.append(result)
        
        # 하루치 현재가 가져오기
        for item in items:
            getIntradayData(item['STOCK_CD'])
    
    def sell(self):
        pass

    def recommend(self):
        
        # 가치분석
        self.valueAnalysis()
        
        # 기술적분석
        result = self.techAnalysis()
        
        return result
        
        
    def recommendStockUpJong(self, type):
        # 일단 properties 에서 업종종류 가져옴
        raws = properties.getSelection(TARGET_PORTFOLIO)[TOIN_CODES].split(",")
        toinCodes = []
        result = []
        for raw in raws:     
            toinCodes.append(raw)
        
        for toinCode in toinCodes:
            cursor = self.dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_TOIN_CD, 
                                                  toinCode)
            stockItems = cursor.fetchall()
            
            # 받아온 종목들을 file 에 저장 (DB에 저장하면 리소스 소모 심함)
            for stockItem in stockItems:
                stockCd = str(stockItem[StockColumn.STOCK_CD])
                stockFilePath = self.path + "/" + stockCd + ".csv"
                
                if not file_util.isFile(stockFilePath):
                    file_util.mkdir(self.path)
                    rows = getHistoricalData(stockCd, self.start, self.end)
                    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                             "Close", "Volume", "Adj Close"])
                    df.to_csv(stockFilePath, index=False)
            
            # techAnalysis 
            # 여기서 pair 종목을 전부 뽑아냄.
            # 리턴 컬럼 sourcePair, targetPair, cointegration, residual, correlationCoefficient
            techResult = self.pairTradingCommon.applyPairTrading(stockItems, type, toinCode)
            result.append(techResult)
        
        return result
    
    def recommendStockGroup(self, type):
        cursor = self.dataHandler.openSql(SELECT_STOCK_GROUP)
        groupItems = cursor.fetchall()
        result = []
        
        for groupItem in groupItems:
            groupCd = groupItem[StockColumn.GROUP_CD]
            cursor = self.dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_GROUP_CD, 
                                                       groupCd)
            stockItems = cursor.fetchall()
            
            # 받아온 종목들을 file 에 저장 (DB에 저장하면 리소스 소모 심함)
            for stockItem in stockItems:
                stockCd = str(stockItem[StockColumn.STOCK_CD])
                stockFilePath = self.path + "/" + stockCd + ".csv"
                
                if not file_util.isFile(stockFilePath):
                    file_util.mkdir(self.path)
                    rows = getHistoricalData(stockCd, self.start, self.end)
                    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                             "Close", "Volume", "Adj Close"])
                    df.to_csv(stockFilePath, index=False)
                        
            techResult = self.pairTradingCommon.applyPairTrading(stockItems, type, groupCd)
            result.append(techResult)
        
        return result
    
    def valueAnalysis(self):
        pass
    
    def techAnalysis(self):
        
        totalResult = {}
        
        if "upJong" in self.types:
            result = self.recommendStockUpJong("upJong")
            totalResult['upJong'] = result
        
        if "group" in self.types:
            result = self.recommendStockGroup("group")
            totalResult['group'] = result
                        
        return totalResult

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