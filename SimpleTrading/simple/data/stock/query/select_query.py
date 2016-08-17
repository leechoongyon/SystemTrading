# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

from enum import Enum


SELECT_TARGET_PORTFOLIO = ("select * from target_portfolio;")
SELECT_LIVE_PORTFOLIO = ("select * from live_portfolio;")
SELECT_STOCK_GROUP = ("select * from stock_group;")
SELECT_STOCK_TOIN = ("select * from stock_toin;")
 
SELECT_STOCK_ITEM_WITH_GROUP_CD = (
"select * "
 + "from stock_item "
 + "where group_cd = %s "
) 
    

SELECT_STOCK_ITEM_WITH_TOIN_CD = (
"select * "
 + "from stock_item "
 + "where toin_cd = %s "
)    

SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO = (
"select b.stock_cd, b.ym_dd, a.market_cd " 
 + "from stock_item a, stock_item_daily b, target_portfolio c " 
 + "where a.stock_cd = b.stock_cd and b.stock_cd = c.stock_cd "
 + "order by b.ym_dd desc "
 + "limit 1;")

if __name__ == '__main__':
    print SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO