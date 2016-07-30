# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 30.

@author: lee
'''

import pandas as pd
from simple.common.util import dataframe_util
from simple.common.util.properties_util import properties, STOCK_DATA
from simple.data.controlway.crawler.data_crawler import getHistoricalData


if __name__ == '__main__':
    
    start = "2014-01-01"
    end = "2016-07-30"
    # kakao = 035720 / combine = 047770
    symbol = "035720"
    
    rows = getHistoricalData(symbol, start, end)
    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                     "Close", "Volume", "Adj Close"])
    df[['Close']] = df[['Close']].apply(pd.to_numeric)
    
    print df
    print df['Close'].iloc[-1]
    
    earningsRate = df['Close'].copy()
    earningsRate[1:] = (earningsRate[1:] / earningsRate[:-1].values) - 1
    earningsRate[0] = 0
    
    
    df['earningsRate'] = earningsRate
    