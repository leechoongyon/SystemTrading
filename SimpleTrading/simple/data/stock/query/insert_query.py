'''
Created on 2016. 7. 25.

@author: lee
'''

INSERT_STOCK_ITEM_DAILY_01 = (
           "INSERT INTO STOCK_ITEM_DAILY " 
                "(STOCK_CD, YM_DD, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, " 
                " CLOSE_PRICE, VOLUME, ADJ_CLOSE_PRICE) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE "
                "YM_DD = VALUES(YM_DD),"
                "OPEN_PRICE = VALUES(OPEN_PRICE), "
                "HIGH_PRICE = VALUES(HIGH_PRICE), "
                "LOW_PRICE = VALUES(LOW_PRICE), "
                "CLOSE_PRICE = VALUES(CLOSE_PRICE), "
                "VOLUME = VALUES(VOLUME), "
                "ADJ_CLOSE_PRICE = VALUES(ADJ_CLOSE_PRICE)"
           )