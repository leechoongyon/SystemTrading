# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 26.

@author: lee
'''
'''
    그룹별 / 업종별 / WICS별 데이터를 수집
    
'''

from simple.data.controlway.crawler.stock_toin_crawler import getAllStockCdThroughDaum


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


if __name__ == '__main__':
    
    # downloadAllStockCode
    '''
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNms = ["kospi", "kosdaq"]
    downloadAllStockCd(path, marketNms)
    '''
    
    # getAllStockCd
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNm = "kospi"
    print getAllStockCd(path, marketNm)