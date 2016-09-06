# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 26.

@author: lee
'''
'''
    그룹별 / 업종별 / WICS별 데이터를 수집
    
'''

import sys

from simple.common.util import string_util
from simple.common.util.time_util import getTodayWithFormatting
from simple.data.controlway.crawler.stock_crawler import getAllStockCdThroughDaum, \
    getBasicStockInfoThroughDaum
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.controlway.db.mysql.data_handler import DataHandler
from simple.data.stock.query.insert_query import INSERT_STOCK_ITEM_01


def downloadAllStockCd(path, marketNms):
    for marketNm in marketNms:
        f = open(path + "/" + marketNm, "w")
        stockCds = getAllStockCdThroughDaum(marketNm)
        for stockCd in stockCds:
            f.write("{}\n".format(stockCd))
        f.close()

def getAllStockCd(path, marketNm):
    f = open(path + "/" + marketNm, "r")
    stockCds = f.readlines()
    f.close()
    return stockCds
    

def collectStockDataForGroup():
    
    '''
        1. crawling 으로 그룹별 데이터를 STOCK_GROUP 테이블에 넣기.
        2. 이 때, 종목들을 뽑아올텐데 이 종목들을 STOCK_ITEM 넣기. 이 때, 가격 + 재무정보 둘 다 업데이트 하고   
    '''
    
    '''
    for group in groups:
        
        for stock in group:
    '''     
            
    
    pass


def collectStockDataForToin():
    pass

def collectStockDataForWics():
    pass


def storeBasicStockInfoInDB(rows):
    dataHandler = data_handler_factory.getDataHandler()
    dataHandler.execSqlManyWithParam(INSERT_STOCK_ITEM_01,
                                           rows)

    data_handler_factory.close(dataHandler)

def convertStockType(rows):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    realRow = []
    index = 0
    for row in rows:
        tempRow = str(unicode(row))
        
        if index == 2:
            if tempRow is '':
                tempRow = 0
            else:
                tempRow = int(tempRow)
        elif index == 3:
            if tempRow is '':
                tempRow = 0
            else:
                tempRow= int(tempRow)
        elif index == 4:
            if tempRow is '':
                tempRow = 0
            else:
                tempRow = int(tempRow)
        elif index == 5 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)    
        elif index == 6 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 7 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 8 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 10 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 12 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        
        index += 1    
        realRow.append(tempRow)
        
    return realRow

def processStockData(tempRows):

    '''
        저장할 목록
        0. 종목코드 (0) / 1. 종목명(1) / 2. 현재가(2) / 3. 52주 고가(13)
        4. 52주 저가 (15) / 5. EPS(28) / 6. BPS(30) / 7. PER(29)
        8. PBR(31) / 9. TOIN(32) / 10. TOIN_PER(26)
        11. WICS(33) / 12. 시가총액(20) / 13. marketType
    '''
    
    rows = []
    for tempRow in tempRows:
        row = [tempRow[0], tempRow[1], tempRow[2], tempRow[13],
               tempRow[15], tempRow[28], tempRow[30], tempRow[29],
               tempRow[31], tempRow[32], tempRow[26], tempRow[33],
               tempRow[20], tempRow[34]]
        realRow = convertStockType(row)
        rows.append(realRow)
        
    return rows


def collectBasicStockInfo():

    # 1. downloadAllStockCode
    #    초기에 한 번 파일을 생성했으면 당분간 또 생성안해도 됨
    '''
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNms = ["kospi", "kosdaq"]
    downloadAllStockCd(path, marketNms)
    '''
    
    # 2. getAllStockCd
    
    
    # kospi
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNm = "kospi"
    rawItems = getAllStockCd(path, marketNm)
    
    kospiStockCd = []
    for rawItem in rawItems:
        stockCd = string_util.sub("\n", "", rawItem)
        kospiStockCd.append(stockCd)

    # kosdaq
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNm = "kosdaq"
    rawItems = getAllStockCd(path, marketNm)
    
    kosdaqStockCd = []
    for rawItem in rawItems:
        stockCd = string_util.sub("\n", "", rawItem)
        kosdaqStockCd.append(stockCd)

    # 3. getBasicStockInfoThroughDaum
    
    '''
         기본주가정보
       0. 종목코드 / 1. 종목명 / 2. 현재가 / 3. 시가 / 4. 전일비 / 5. 고가 / 6. 등락률
       7. 저가 / 8. 거래량 / 9. 매도 / 10. 거래대금 / 11. 매수
       12. 상한가 / 13. 52주 고가 / 14. 하한가 / 15. 52주 저가 / 16. 연중 최고가
       17. 50일 고가 / 18. 연중 최저가 / 19. 50일 저가 / 20. 시가총액 / 21. 자본금
       22. 상장주식수 / 23. 액면가 / 24. 결산월 / 25. 상장일 / 26. 업종 PER
       27. PER / 28.EPS / 29. PER / 30. BPS / 31. PBR / 32. 업종
       33. WICS / 34. marketType
    '''

    # kospi
    rows = []
    for stockCd in kospiStockCd:
        row = getBasicStockInfoThroughDaum(stockCd, "kospi")
        rows.append(row)
    
    # kosdaq
    
    for stockCd in kosdaqStockCd:
        row = getBasicStockInfoThroughDaum(stockCd, "kosdaq")
        rows.append(row)
    
    # 4. StockData 가공
    '''
        저장할 목록
        0. 종목코드 (0) / 1. 종목명(1) / 2. 현재가(2) / 3. 52주 고가(13)
        4. 52주 저가 (15) / 5. EPS(28) / 6. BPS(30) / 7. PER(29)
        8. PBR(31) / 9. TOIN(32) / 10. TOIN_PER(26)
        11. WICS(33) / 12. 시가총액(20) / 13. marketType
    '''
    rows = processStockData(rows)
    
    # 5. StoreBasicStockInfoInDB
    storeBasicStockInfoInDB(rows)

def collectFinancialStockInfo():
    pass

if __name__ == '__main__':
    
    # 1. 종목기본정보 가져오기 
    collectBasicStockInfo()

    # 2. 재무정보 가져오기
    collectFinancialStockInfo()

    

