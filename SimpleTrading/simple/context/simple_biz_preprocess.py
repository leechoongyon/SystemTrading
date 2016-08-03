# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import datetime
import time

from simple.common.util.properties_util import properties, DB_DATA, STOCK_DATA, \
    CRAWLER, BIZ_PRE_PROCESS, MARKET_OPEN_TIME, MARKET_CLOSE_TIME, \
    TARGET_DATA_LOAD, LIVE_DATA_LOAD, TARGET_DATA_LOAD_PERIOD
from simple.common.util.time_util import getTodayWithFormatting, \
    getDayFromSpecificDay, convertStringToDatetime, \
    convertStringToTime, getDayFromSpecificDay, getTodayWithFormatting
from simple.data.controlway.crawler import data_crawler
from simple.data.controlway.crawler.data_crawler import PAGE_NUM, \
    getTotalPageNum, getHistoricalData 
from simple.data.controlway.dataframe import process_dataframe
from simple.data.controlway.dataframe.process_dataframe import getStockDataUsingDatareader, registerStockDataInDb, \
                                                                registerStockDataInDb
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.controlway.db.factory.data_handler_factory import getDataHandler, \
    close
from simple.data.controlway.db.mysql.data_handler import DataHandler
from simple.data.stock import process_stock_data
from simple.data.stock.process_stock_data import getTargetPortfolio, \
    insertTargetPortfolioStockData, \
    getLivePortfolio, insertLivePortfolioStockData
from simple.data.stock.query.insert_query import INSERT_TARGET_PORTFOLIO_01
from simple.data.stock.stock_data import StockColumn, \
    stock_data, StockTable
from simple.portfolio import target_portfolio


def init():
    tempMarketOpenTime = properties.getSelection(STOCK_DATA)[MARKET_OPEN_TIME]
    tempMarketCloseTime = properties.getSelection(STOCK_DATA)[MARKET_CLOSE_TIME]
    
    marketTime = tempMarketOpenTime.split(":")
    hour = int(marketTime[0])
    min = int(marketTime[1]) 
    marketOpenTime = datetime.time(hour, min, 0, 0)
     
    marketTime = tempMarketCloseTime.split(":")
    hour = int(marketTime[0])
    min = int(marketTime[1]) 
    marketCloseTime = datetime.time(hour, min, 0, 0)
     
    stock_data.dict[MARKET_OPEN_TIME] = marketOpenTime 
    stock_data.dict[MARKET_CLOSE_TIME] = marketCloseTime



def preProcess():
    
    print "preProcess starting"
    
    # 0. STOCK_RELATED_DATA init
    init()
    
    dataHandler = data_handler_factory.getDataHandler()
    
    '''
      1.2 타겟포트폴리오 종목 선정
       1.2.1 업종별 코드 테이블 조회해서 업종별 코드 가져오기.
       1.2.2 각 업종에 해당하는 종목 받아오기
       1.2.3 각 종목에 해당하는 2~3년치 데이터 가져옴.
       1.2.4 받아온 업종별 데이터에 대한 표준편차, 분산 구하기 (수익률에 대한)
       1.2.5 재무재표 비교 (업종별 평균 이하는 다 버림)
       1.2.6 추출된 것 중 박스권 최저 10~20% 추출
       1.2.7 여기서 추출된 것을 페어트레이딩 돌리기.
    '''    
        
    refinedDf = target_portfolio.selectionOfStockItems()
    rows = []
    for row in refinedDf.itertuples(index=False):
        rows.append(tuple(row))
    
    dataHandler.execSqlManyWithParam(INSERT_TARGET_PORTFOLIO_01, rows)
    data_handler_factory.close(dataHandler)
    
    
if __name__ == '__main__':
    print "simple_biz_preprocess test"
#     pre_process()
    