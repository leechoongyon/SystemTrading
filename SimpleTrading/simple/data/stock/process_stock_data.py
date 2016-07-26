# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 18.

@author: lee
'''
import time

from simple.common.util import dataframe_util, string_util
from simple.common.util.properties_util import properties, CRAWLER
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler import data_crawler
from simple.data.controlway.crawler.data_crawler import PAGE_NUM
from simple.data.controlway.dataframe.process_dataframe import getStockDataUsingDatareader, \
    registerStockDataInDb
from simple.data.controlway.db.factory.data_handler_factory import getDataHandler
from simple.data.stock.query.insert_query import INSERT_STOCK_ITEM_DAILY_01
from simple.data.stock.query.select_query import SELECT_TARGET_PORTFOLIO
from simple.data.stock.stock_data import StockColumn


# TARGET PORTFOLIO 가져오기
def getTargetPortfolio(dataHandler):
    cursor = dataHandler.openSql(SELECT_TARGET_PORTFOLIO)
    stockItems = cursor.fetchall()
    return stockItems

# TARGET PORTFOLIO 데이터를 STOCK_ITEM_DAILY 테이블에 저장
def insertTargetPortFolioStockData(stockItems, dataHandler):
     for stockItem in stockItems:
        start = getDayFromSpecificDay(time.time(), -700, "%Y%m%d")
        end = getTodayWithFormatting("%Y%m%d")
        pageNum = properties.getSelection(CRAWLER)[PAGE_NUM]
        totalPageNum = data_crawler.getTotalPageNum(stockItem[StockColumn.STOCK_CD],
                                     start, end, pageNum)
        rows = data_crawler.getHistoricalData(stockItem[StockColumn.STOCK_CD],
                                              start, end, int(pageNum), int(totalPageNum))
        dataHandler.execSqlManyWithParam(INSERT_STOCK_ITEM_DAILY_01,
                                           rows)
# stock_item_daily에 대한 가공
def processStockData(df, stockCd):

    dataframe_util.insert(df, 0, 'STOCK_CD', stockCd)
    
    indexs = df.index
    indexs = indexs.format()
    indexs = string_util.replace(indexs, "-", "")
    dataframe_util.insert(df, 1, 'YM_DD', indexs)
    columns={"Open":"OPEN_PRICE","High":"HIGH_PRICE", "Low":"LOW_PRICE", "Close":"CLOSE_PRICE", "Adj Close":"ADJ_CLOSE_PRICE"}
    df = dataframe_util.rename(df, columns)
    return df

# stock_item_daily에 대한 가공2 (data_crawler CRAWLER에서 사용)
def processStockData2(df, stockCd):
    dataframe_util.insert(df, 0, 'STOCK_CD', stockCd)
    columns = {"Date":"YM_DD","Open":"OPEN_PRICE","High":"HIGH_PRICE", "Low":"LOW_PRICE", "Close":"CLOSE_PRICE", "Adj Close":"ADJ_CLOSE_PRICE"}
    df = dataframe_util.rename(df, columns)
    return df
    
if __name__ == '__main__':
    
    print "test"

    '''
        
    # Stock 데이터를 한꺼번에 DB에 밀어넣는다.
    start = "20140101"
    end = "20160718"
    
    # 079160 : CJ CGV /  KaKao : 035720
#     stock_cds = ["079160", "035720"]
#     market_cds = ["KOSPI", "KOSDAQ"]
    stock_cd = "035720"
    market_cd = "KOSDAQ"
    table_nm = "STOCK_ITEM_DAILY"
    exists_option = "append"
    db = "mysql"
    data_handler = getDataHandler()
    con = data_handler.get_conn()
    
    df = getStockDataUsingDatareader(stock_cd, market_cd, start, end)
    df = processStockData(df, stock_cd)
    registerStockDataInDb(con, df, table_nm, exists_option, db)
    
    data_handler.close()
    
    '''