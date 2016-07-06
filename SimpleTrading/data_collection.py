'''
Created on 2016. 7. 1.

@author: lee
'''

import pandas_datareader.data as web
from simple.db.mysql.data_handler import DataHandler

class DataCollection():
    
    def __init__(self, data_handler):
        self.data_handler = data_handler
    
    def collectStockPrice(self, sql, codes, start, end):
        # 1. 종목별로 start ~ end 단위로 price 가져오기        
        for code in codes:
            try:
                df = web.DataReader("%s.KS" % (code), "yahoo", start, end)
                df.insert(0, 'STOCK_CD', code)
                df.insert(0, 'Date', df.index.strftime("%Y%m%d"))
                tuples = [tuple(x) for x in df.to_records(index=False)]
                self.dataHandler.execSqlManyWithParam(sql, tuples)
            except Exception as e:
                print "ERROR occured. Code : %s " % code
                print e
    
