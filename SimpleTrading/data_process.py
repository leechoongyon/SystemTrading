# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 30.

@author: lee

@desc : Daily 데이타를 가져와서 STOCK_ITEM_DAILY에 넣자.

'''
import datetime
import time

import pandas_datareader.data as web
from simple.data.controlway.db.mysql.data_handler import DataHandler


class DataProcess():

    select_stock_item_sql = "SELECT * FROM STOCK_ITEM"
    select_24c_whin_lwst_price_sql = "SELECT MIN(CLOSE_PRICE) FROM STOCK_ITEM_DAILY WHERE STOCK_CD = %(stock_cd)s and YM_DD between %(start)s and %(end)s" 
    insert_stock_item_daily = ("INSERT INTO STOCK_ITEM_DAILY "
                            "(YM_DD, STOCK_CD, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, ADJ_CLOSE_PRICE, VOLUME) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    update_stock_item_m24c_whin_lwst_price_sql = ("UPDATE STOCK_ITEM set M24C_WHIN_LWST_PRICE = %(m24c_whin_lwst_price)s where STOCK_CD = %(stock_cd)s")
    
    def __init__(self, dataHandler):
        self.dataHandler = dataHandler

    def decideM24CWhinLwstPrice(self, sql, codes, start, end):
        try:
            update_params = {}
            
            for code in codes:
                select_param = {'stock_cd':code, 'start':start, 'end':end}
                results = self.dataHandler.execSql(self.select_24c_whin_lwst_price_sql, select_param)
                result = results[0]
                update_param = {'m24c_whin_lwst_price':result[0], 'stock_cd':code}
                update_params.add(update_param)
            self.dataHandler.execSqlManyexecSqlManyWithParame_params)
        
        except Exception, e:
            print "Error decideM24CWhinLwstPrice codes : %s" % code
            print e
    
    def getStockCodes(self, market_type):
        cursor = self.dataHandler.openSql(self.select_stock_item_sql)
        results = cursor.fetchall()
        codes = []
        for result in results:
            codes.append(result[0])
            
        return codes
                
    def getStockGroupCodes(self, sql):
        cursor = self.dataHandler.openSql(sql)
        results = cursor.fetchall()
        group_codes = []
        for result in results:
            codes.append(result[0])
        return group_codes
    
if __name__ == '__main__':
    
    host = "112.150.214.10"
    user = "InsanelySimple"
    passwd = "1234"
    db = "stock"
    charset = "utf8"
    use_unicode = True

    # common init
    data_handler = DataHandler(host, user, passwd, db, charset, use_unicode)
    data_process = DataProcess(data_handler)

    # 1 : KOSPI, 2 : KOSDAQ
    codes = data_process.getStockCode(1)
 
    yesterday = datetime.date.fromtimestamp(time.time() - 1*60*60*24)
    today = datetime.date.fromtimestamp(time.time())
    start = datetime.datetime(yesterday.year, yesterday.month, yesterday.day)
    end = datetime.datetime(today.year, today.month, today.day)
    
    # start ~ end 까지의 종목별 Prices를 Pandas를 통해 가져온다.
    data_process.collectStockPrice(data_process.insert_stock_item_daily, codes, start, end)
    
    # 2년내 최저가 결정
    # STOCK_ITEM_DAILY를 코드별로 검색하면서 최저가격을 쿼리로 찾으면 되겠지
    before_m24c = datetime.date.fromtimestamp(time.time() - 730*60*60*24)
    today = datetime.date.fromtimestamp(time.time())
    start = datetime.datetime(before_m24c.year, before_m24c.month, before_m24c.day)
    end = datetime.datetime(today.year, today.month, today.day)
    
    
    data_process.decideM24CWhinLwstPrice(data_process.update_stock_item_m24c_whin_lwst_price_sql, 
                                 codes, 
                                 start.strftime("%Y%m%d"), 
                                 end.strftime("%Y%m%d"))
    
    # finalize
    data_process.close() 