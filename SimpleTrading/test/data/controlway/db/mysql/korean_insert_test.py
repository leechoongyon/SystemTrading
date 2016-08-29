# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 29.

@author: lee
'''
from simple.data.controlway.db.factory import data_handler_factory

if __name__ == '__main__':
    
    '''
    sql = (
           "INSERT INTO TEST "
                "(C) "
            "VALUES (%s)"           
           )
    
    rows = []
    rows.append("한글")
    rows.append("한글1")
    rows.append("한글2")
    print rows
    dataHandler = data_handler_factory.getDataHandler()
    dataHandler.execSqlManyWithParam(sql, rows)
    data_handler_factory.close(dataHandler)
    '''
    
    
    insertQuery = (
                   "INSERT INTO STOCK_ITEM " 
                        "(STOCK_CD, STOCK_NM, CUR_PRICE, 52WEEK_HIGH_PRICE, "
                        " 52WEEK_LOW_PRICE, EPS, BPS, PER, PBR, "
                        " TOIN, TOIN_PER, WICS, MARKET_CAPITALIZATION, LST_RVSE_DT)"
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,sysdate) "
                    )
    
    row1 = ['006360', 'GS\xea\xb1\xb4\xec\x84\xa4', '28850', '31800', '18650', '367', '47215', '78.61', '0.61', '\xea\xb1\xb4\xec\x84\xa4\xec\x97\x85', '-18.06', '\xea\xb1\xb4\xec\x84\xa4', '20484', '20160829']
    row2 = ['035720', '\xec\xb9\xb4\xec\xb9\xb4\xec\x98\xa4', '79300', '136000', '79300', '1269', '42476', '62.49', '1.87', '\xec\x9d\xb8\xed\x84\xb0\xeb\x84\xb7', '55.33', '\xec\x9d\xb8\xed\x84\xb0\xeb\x84\xb7\xec\x86\x8c\xed\x94\x84\xed\x8a\xb8..', '53537', '20160829']

    rows = []
    rows.append(row1)
    dataHandler = data_handler_factory.getDataHandler()
    dataHandler.execSqlManyWithParam(insertQuery, rows)
    data_handler_factory.close(dataHandler)

