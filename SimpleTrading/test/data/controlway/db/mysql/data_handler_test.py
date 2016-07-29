# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 25.

@author: lee
'''
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.select_query import SELECT_STOCK_ITEM_WITH_PARAM


if __name__ == '__main__':
    
    '''
    # insert example
    
    insert_stock_item_daily = ("INSERT INTO STOCK_ITEM_DAILY "
                            "(YM_DD, STOCK_CD, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, ADJ_CLOSE_PRICE, VOLUME) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data_handler = data_handler_factory.getDataHandler()
    
    tuple1 = (100, 200)
    tuple2 = (100, 300)
    rows = [("100", "200"), ("100","300"), ("100","500")]
    print rows
    # sql = "INSERT INTO TEST (A,B) VALUES (%s,%s)"
    sql = ("INSERT INTO TEST (A,B) " 
            "VALUES (%s,%s) "
            "ON DUPLICATE KEY UPDATE "
            "B = VALUES(B)"
            )
    data_handler.execSqlManyWithParam(sql, rows)
    data_handler_factory.close(data_handler)
    '''
    
    
    # selectWithParam example
    dataHandler = data_handler_factory.getDataHandler()
    cursor = dataHandler.execSqlWithParam(SELECT_STOCK_ITEM_WITH_PARAM, "기계")
    stockItems = cursor.fetchall()
    for stockItem in stockItems:
        print stockItem['STOCK_GROUP_CD']