# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

from enum import Enum



    
SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO = (
"select a.stock_cd, a.ym_dd, a.open_price, a.high_price, a.low_price, a.close_price, a.ADJ_CLOSE_PRICE, a.volume " 
 + "from stock_item_daily a, target_portfolio b " 
 + "where a.stock_cd = b.stock_cd "
 + "order by a.ym_dd desc "
 + "limit 1;")

if __name__ == '__main__':
    print SELECT_JOIN_STOCK_ITEM_DAILY_AND_TARGET_PORTFOLIO