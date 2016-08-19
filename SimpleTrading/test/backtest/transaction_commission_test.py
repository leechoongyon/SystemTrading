'''
Created on 2016. 8. 19.

@author: lee
'''

import datetime

import pandas_datareader.data as web

from zipline.algorithm import TradingAlgorithm
from zipline.api import symbol, order_target, set_commission, commission

def initialize(context):
    set_commission(commission.PerDollar(cost=0.00165))

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
    
    algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
    results = algo.run(gs)
    
    print results[['starting_cash', 'ending_cash', 'ending_value']]