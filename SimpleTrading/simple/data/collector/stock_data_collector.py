# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 26.

@author: lee
'''
'''
    그룹별 / 업종별 / WICS별 데이터를 수집
    
'''

from simple.data.controlway.crawler.stock_crawler import getAllStockCdThroughDaum,\
    getBasicStockInfoThroughDaum


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


def storeBasicStockInfoInDB(row):
    


if __name__ == '__main__':
    
    # 1. downloadAllStockCode
    #    초기에 한 번 파일을 생성했으면 당분간 또 생성안해도 됨
    '''
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNms = ["kospi", "kosdaq"]
    downloadAllStockCd(path, marketNms)
    '''
    
    # 2. getAllStockCd
    '''
    path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data"
    marketNm = "kospi"
    print getAllStockCd(path, marketNm)
    '''
    
    
    # 3. getBasicStockInfoThroughDaum
    '''
         기본주가정보
       0. 현재가 / 1. 시가 / 2. 전일비 / 3. 고가 / 4. 등락률
       5. 저가 / 6. 거래량 / 7. 매도 / 8. 거래대금 / 9. 매수
       10. 상한가 / 11. 52주 고가 / 12. 하한가 / 13. 52주 저가 / 14. 연중 최고가
       15. 50일 고가 / 16. 연중 최저가 / 17. 50일 저가 / 18. 시가총액 / 19. 자본금
       20. 상장주식수 / 21. 액면가 / 22. 결산월 / 23. 상장일 / 24. 업종 PER
       25. PER
    '''
    
    stockCd = "006360"
    row = getBasicStockInfoThroughDaum(stockCd)
    
    # 4. StoreBasicStockInfoInDB
    '''
        저장할 목록
        1. 현재가 (0) / 2. 52주 고가 (11) / 3. 52주 저가 (13) / 4. 시가총액 (18) / 5. 업종 PER (24)
        6. PER (25) 
    '''
    storeBasicStockInfoInDB(row)
    