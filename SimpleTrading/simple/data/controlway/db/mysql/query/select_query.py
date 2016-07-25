# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

from enum import Enum


SELECT_TARGET_PORTFOLIO = ("select * from target_portfolio;")


    
SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO = (
"select b.stock_cd, b.ym_dd, a.market_cd " 
 + "from stock_item a, stock_item_daily b, target_portfolio c " 
 + "where a.stock_cd = b.stock_cd and b.stock_cd = c.stock_cd "
 + "order by b.ym_dd desc "
 + "limit 1;")

if __name__ == '__main__':
    print SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO