# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
import time

import pandas as pd
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DOWNLOAD_PATH, STOCK_DATA
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getHistoricalData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_STOCK_ITEM_WITH_PARAM
from simple.strategy.pairtrading.common.pairtrading import applyPairTrading


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
    
    columns = ['STOCK_CD', 'CURR_PRICE', 'HIGH', 'LOW', 'VAR', 'STD']
    refinedDf = pd.DataFrame(columns=columns)
    count = 0

    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]
    
    
    
    for toinItem in toinItems:
        dataHandler = data_handler_factory.getDataHandler()
        cursor = dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_PARAM, toinItem)
        stockItems = cursor.fetchall()
        
        for stockItem in stockItems:
            rows = getHistoricalData(stockItem['STOCK_CD'], start, end)
            df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                     "Close", "Volume", "Adj Close"])
            df.to_csv(path + "/" + stockItem["STOCK_CD"] + ".csv", index=False)
            
        for stockItem in stockItems:
#             rows = getHistoricalData(stockItem['STOCK_CD'], start, end)
            df = pd.read_csv(path + "/" + stockItem['STOCK_CD'] + ".csv")
            df[['Close']] = df[['Close']].apply(pd.to_numeric)
            closeMax = df['Close'].max()
            closeMin = df['Close'].min()
            currPrice = df['Close'][0]
            earningsRate = df['Close'].copy()
            earningsRate[1:] = (earningsRate[1:] / earningsRate[:-1].values) - 1
            earningsRate[0] = 0
            var = earningsRate.var()
            std = earningsRate.std()
            refinedDf.loc[count] = [stockItem['STOCK_CD'], currPrice, closeMax, closeMin, var, std]
            count += 1
            
            # 1차 재무정보 가져와서 비교
            # 영업이익, 매출액, PBR, PER이 업종평균과 비교하면 어떤지
            
            # 2차 LOW와 CURR_PRICE 비교해서 차이가 10~20% 정도 되는지
            # 추후에 1.2를 옵션으로 조절하기
            refinedDf = refinedDf[refinedDf['LOW'] * 1.2 > refinedDf['CURR_PRICE']]
            
            # 3차 PairTrading
            '''
                페어트레이딩을 하기 위해선 선택된 종목과 그 종목에 해당하는 다른 업종들의 Close 데이터가 필요하다.
                미리 업종을 for문 돌릴 때 그 업종에 해당하는 데이터를 전부 파일로 만들기.
           refinedDf를 for문으로 돌릴 때 저 위쪽에 stockItems 가 있으니 그 stockITems와 같이 for문을 돌리면 되겠네.
                자기건 뺴고 돌리면 될듯. 돌리면서 Cointegration과 상관계수를 구해서 어느 일정 이상 되는지 판단하고 실제 그게 저평가인지 아닌지는 보팅기법을 써야겠지. 
            '''
            
        for stockCd in refinedDf['STOCK_CD']:
            for preparatoryStockItem in stockItems:
                if (stockCd != preparatoryStockItem['STOCK_CD']):
                    print "pair : %s \t %s" % (stockCd, preparatoryStockItem['STOCK_CD'])
                    statistics = applyPairTrading(stockCd, preparatoryStockItem
                                     , start, end, path)
                    
        
    return refinedDf
    
    
if __name__ == '__main__':
    print selectionOfStockItems()    