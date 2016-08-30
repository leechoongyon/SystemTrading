'''
Created on 2016. 7. 25.

@author: lee
'''

INSERT_STOCK_ITEM_01 = (
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

INSERT_TARGET_PORTFOLIO_01 = (
    "INSERT INTO TARGET_PORTFOLIO " 
        "(STOCK_CD, DD01_BEFR_YMD_PRICE, HIGH_PRICE, "
          "LOW_PRICE, REGST_YMD, ETC) "
    "VALUES (%s, %s, %s, %s, %s, %s) "
        "ON DUPLICATE KEY UPDATE "
        "DD01_BEFR_YMD_PRICE = VALUES(DD01_BEFR_YMD_PRICE), "
        "HIGH_PRICE = VALUES(HIGH_PRICE), "
        "LOW_PRICE = VALUES(LOW_PRICE), "
        "REGST_YMD = VALUES(REGST_YMD), "
        "ETC = VALUES(ETC)"                          
)