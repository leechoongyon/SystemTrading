# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 19.

@author: lee
'''

import pandas_datareader.data as web
import pandas_datareader.data as web
import datetime
from zipline.api import order_target, record, symbol
from zipline.algorithm import TradingAlgorithm
import matplotlib.pyplot as plt
from zipline.api import set_commission, commission


def initialize(context):
    set_commission(commission.PerDollar(cost=0.00165))
    pass

def handle_data(context, data):
    sym = symbol('GS')
    order_target(sym, 1)
    
if __name__ == '__main__':
    start = datetime.datetime(2016, 1, 1)
    end = datetime.datetime(2016, 1, 31)
    gs = web.DataReader("078930.KS", "yahoo", start, end)
    gs = gs[['Adj Close']]
    gs.columns = ['GS']
    gs = gs.tz_localize("UTC")
    
    # 초기 투자 금액 capital_base 로 설정
    algo = TradingAlgorithm(capital_base=100000000, initialize=initialize, handle_data=handle_data, identifiers=['GS'])
    results = algo.run(gs)
    print results[['starting_cash', 'ending_cash', 'ending_value']]