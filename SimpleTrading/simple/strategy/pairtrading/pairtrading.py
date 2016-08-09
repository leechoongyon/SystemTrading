# -*- coding: utf-8 -*-

'''
Created on 2016. 8. 2.

@author: lee
'''

import time

import pandas as pd
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DOWNLOAD_PATH, STOCK_DATA, TARGET_PORTFOLIO, \
    TOIN_CODES
from simple.common.util.stats_util import getLogSpreadResidual, \
    getCointegrationUsingLog, getCorrelationCoefficientUsingLog
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler.data_crawler import getIntradayData, \
    getHistoricalData
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_TARGET_PORTFOLIO, \
    SELECT_STOCK_ITEM_WITH_PARAM
from simple.data.stock.stock_data import StockColumn
from simple.strategy.pairtrading.common.pair_trading_common import applyPairTrading


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
    
    columns = ['STOCK_CD', 'DD01_BEFR_YMD_PRICE', 'HIGH_PRICE', 'LOW_PRICE', 'REGST_YMD', 'ETC']
    refinedDf = pd.DataFrame(columns=columns)
    count = 0

    # 1. 업종별 테이블 조회
    # 일단 테스트를 위해 properties 정의된 업종만 조회
    raws = properties.getSelection(TARGET_PORTFOLIO)[TOIN_CODES].split(",")
    
    toinCodes = []
    for raw in raws:     
        toinCodes.append(raw)

    
    # 2. 업종별코드를 이용해 해당 업종에 대한 종목을 전체 조회 (STOCK_ITEM)
    for toinCode in toinCodes:
        fncStdPassCount = 0

        print "toinCode : %s " % toinCode

        dataHandler = data_handler_factory.getDataHandler()
        cursor = dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_PARAM, 
                                              toinCode)
        stockItems = cursor.fetchall()
        
        # 2.1 받아온 종목들을 file 에 저장 (DB에 저장하면 리소스 소모 심함)
        for stockItem in stockItems:
            rows = getHistoricalData(stockItem[StockColumn.STOCK_CD], start, end)
            df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                     "Close", "Volume", "Adj Close"])
            df.to_csv(path + "/" + stockItem[StockColumn.STOCK_CD] + ".csv", index=False)
            
        # 2.2 여기에 재무기준이 들어가야함.
        for stockItem in stockItems:
            df = pd.read_csv(path + "/" + stockItem[StockColumn.STOCK_CD] + 
                             ".csv")
            df[['Close']] = df[['Close']].apply(pd.to_numeric)
            closeMax = df['Close'].max()
            closeMin = df['Close'].min()
            currPrice = df['Close'][0]
            earningsRate = df['Close'].copy()
            earningsRate[1:] = (earningsRate[1:] / earningsRate[:-1].values) - 1
            earningsRate[0] = 0
            var = earningsRate.var()
            std = earningsRate.std()
            
            if currPrice < (closeMin * 1.2): 
                refinedDf.loc[count] = [stockItem[StockColumn.STOCK_CD], 
                                        currPrice, closeMax, 
                                        closeMin, end, 
                                        'Recommended by targetalgorithm']
                count += 1
                fncStdPassCount += 1
            
            # 1차 재무정보 가져와서 비교
            # 영업이익, 매출액, PBR, PER이 업종평균과 비교하면 어떤지
            
            # 2차 LOW와 CURR_PRICE 비교해서 차이가 10~20% 정도 되는지
            # 추후에 1.2를 옵션으로 조절하기
            
            # 3차 PairTrading
            '''
                페어트레이딩을 하기 위해선 선택된 종목과 그 종목에 해당하는 다른 업종들의 Close 데이터가 필요하다.
                미리 업종을 for문 돌릴 때 그 업종에 해당하는 데이터를 전부 파일로 만들기.
           refinedDf를 for문으로 돌릴 때 저 위쪽에 stockItems 가 있으니 그 stockITems와 같이 for문을 돌리면 되겠네.
                자기건 뺴고 돌리면 될듯. 돌리면서 Cointegration과 상관계수를 구해서 어느 일정 이상 되는지 판단하고 실제 그게 저평가인지 아닌지는 보팅기법을 써야겠지. 
            '''
            
        for stockCd in refinedDf[count - fncStdPassCount :][StockColumn.STOCK_CD]:
            statiDf = pd.DataFrame(columns=['cointegration', 'residual', 'correlationCoefficient'])
            index = 0
            for preparatoryStockItem in stockItems:
                if (stockCd != preparatoryStockItem[StockColumn.STOCK_CD]):
                    stati = applyPairTrading(str(stockCd), 
                                             str(preparatoryStockItem[StockColumn.STOCK_CD]),
                                             start, end, path)
                    
                    statiDf.loc[index] = [stati[0], 
                                          stati[1],
                                          stati[2]] 
                    index += 1
                    
                    
                    
            # 통계를 보고 해당 종목을 제외할지 결정
            # cointegration 0.5 이상 / residual 0 이하일 때 적용
            # 이를 Voting 기법 이용
            
            # cointegration이 0.5인것만 일단 count 한 뒤에 residual 이 0 이하인 것이랑 비교해서 저평가인지 판단. 
            
            votingCount = 0
            totalRows = statiDf['cointegration'].count()
            for index, row in statiDf.iterrows():
                if row['cointegration'] > 0.5:
                    if row['residual'] < 0:
                        votingCount += 1
            
            if votingCount < (totalRows / 2):
                refinedDf = refinedDf[refinedDf[StockColumn.STOCK_CD] != stockCd]
                
    return refinedDf

def valueAnalysis():
    pass

def techAnalysis():
    pass

if __name__ == '__main__':
    
    '''
            통신업
        017670
        030200
        032640
    '''
    
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]
    print applyPairTrading('017670', '030200', start, end, path)