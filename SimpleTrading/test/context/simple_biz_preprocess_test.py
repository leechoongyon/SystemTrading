'''
Created on 2016. 8. 3.

@author: lee
'''


if __name__ == '__main__':
    
    '''
        1. TARGET_PORTFOLIO 읽어오기
         1.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기 
        2. LIVE_PORTFOLIO 읽어오기
         2.1 읽어온 종목코드의 STOCK_ITEM_DEILY 최신 YM_DD 읽어오기
        3. 읽어온 종목 코드들의 최신 YM_DD를 가지고   
    '''
    
    # 1. TARGET_PORTFOLIO 선처리
    #  1.1 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    isTargetDataLoad = properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD]
    if "True" == isTargetDataLoad:
        print "executing target data load"
        dataHandler = data_handler_factory.getDataHandler()
        stockItems = getTargetPortfolio(dataHandler)
        startNum = properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD]
        insertTargetPortfolioStockData(stockItems, dataHandler, startNum)
        data_handler_factory.close(dataHandler)
    
        
    # 2. LIVE_PORTFOLIO 선처리
    #  2.2 PORTFOLIO에 있는 종목 DAILY_DATA 최신화
    isLiveDataLoad = properties.getSelection(BIZ_PRE_PROCESS)[LIVE_DATA_LOAD]
    if "True" == isLiveDataLoad:
        print "executing live data load"
        dataHandler = data_handler_factory.getDataHandler()
        stockItems = getLivePortfolio(dataHandler)
        insertLivePortfolioStockData(stockItems, dataHandler)
        data_handler_factory.close(dataHandler)