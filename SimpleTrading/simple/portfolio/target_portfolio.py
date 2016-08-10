# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
import time

from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DATA, STOCK_DOWNLOAD_PATH, TARGET_PORTFOLIO, \
    TYPES
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.db.factory import data_handler_factory
from simple.strategy.pairtrading import pairtrading, pair_trading
from simple.strategy.pairtrading.pair_trading import PairTrading


def preProcess():
    pass

def postProcess():
    pass

def perform():

    preProcess()
    
    '''
        1. TARGET_PORTFOLIO 
         1.1 추천된 종목을 언제 살지 매수 타이밍을 알아본다.
          1.1.1 타겟포트폴리오 종목 가져오기
          1.1.2 해당 종목 현재가 가져오기
          1.1.3 그 종목의 볼린저밴드, 기타 등등 비교
    '''
    
    # 여기엔 전략의 Buy 가 오면 됨.
    pairtrading.buy()
    
    
    
        
    postProcess()
    
    
def selectionOfStockItems():
    
    # 각 전력의 Recommend 가 여기에 위치
    dataHandler = data_handler_factory.getDataHandler()
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH] + "/" + end
    types = properties.getSelection(TARGET_PORTFOLIO)[TYPES]
    
    pairTrading = PairTrading(start, end, path, dataHandler, types)
    recommend = pairTrading.recommend()
    
    
    return recommend
    
if __name__ == '__main__':
#     print selectionOfStockItems()
#     perform()    

    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH] + "/" + end
    print path