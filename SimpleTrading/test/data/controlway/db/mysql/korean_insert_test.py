# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 29.

@author: lee
'''
import sys

from simple.data.controlway.db.factory import data_handler_factory
from simple.common.util import string_util



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
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now()) "
            "ON DUPLICATE KEY UPDATE "
                "STOCK_NM = VALUES(STOCK_NM),"
                "CUR_PRICE = VALUES(CUR_PRICE), "
                "52WEEK_HIGH_PRICE = VALUES(52WEEK_HIGH_PRICE), "
                "52WEEK_LOW_PRICE = VALUES(52WEEK_LOW_PRICE), "
                "EPS = VALUES(EPS), "
                "BPS = VALUES(BPS), "
                "PER = VALUES(PER), "
                "PBR = VALUES(PBR), "
                "TOIN = VALUES(TOIN), "
                "TOIN_PER = VALUES(TOIN_PER), "
                "WICS = VALUES(WICS), "
                "MARKET_CAPITALIZATION = VALUES(MARKET_CAPITALIZATION), "
                "LST_RVSE_DT = VALUES(LST_RVSE_DT)"
           )
    
    row1 = ['006360', 'GS\xea\xb1\xb4\xec\x84\xa4', '28850', '31800', '18650', '367', '47215', '78.61', '0.61', '\xea\xb1\xb4\xec\x84\xa4\xec\x97\x85', '-18.06', '\xea\xb1\xb4\xec\x84\xa4', '20484']
    row2 = ['035720', '\xec\xb9\xb4\xec\xb9\xb4\xec\x98\xa4', '79300', '136000', '79300', '1269', '42476', '62.49', '1.87', '\xec\x9d\xb8\xed\x84\xb0\xeb\x84\xb7', '55.33', '\xec\x9d\xb8\xed\x84\xb0\xeb\x84\xb7\xec\x86\x8c\xed\x94\x84\xed\x8a\xb8..', '53537']

    '''
        저장할 목록
        0. 종목코드 (0) / 1. 종목명(1) / 2. 현재가(2) / 3. 52주 고가(13)
        4. 52주 저가 (15) / 5. EPS(28) / 6. BPS(30) / 7. PER(29)
        8. PBR(31) / 9. TOIN(32) / 10. TOIN_PER(26)
        11. WICS(33) / 12. 시가총액(20)
    '''

    rows = []
    rows.append(row1)

    reload(sys)
    sys.setdefaultencoding('utf-8')
    r = range(0,13)
    for row in rows:
        for i in r:
            row[i] = str(unicode(row[i]))

    row1[2] = int(row1[2])
    row1[3] = int(row1[3])
    row1[4] = int(row1[4])
    row1[5] = float(row1[5])
    row1[6] = float(row1[6])
    row1[7] = float(row1[7])
    row1[8] = float(row1[8])
    row1[10] = float(row1[10])
    row1[12] = float(row1[12])
    
    dataHandler = data_handler_factory.getDataHandler()
    dataHandler.execSqlManyWithParam(insertQuery, rows)
    data_handler_factory.close(dataHandler)