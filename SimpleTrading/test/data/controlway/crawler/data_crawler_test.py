# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 29.

@author: lee
'''
from simple.data.controlway.crawler.data_crawler import getHistoricalData

import pandas as pd

if __name__ == '__main__':
    start = "2014-01-01"
    end = "2016-07-25"
    # kakao = 035720 / combine = 047770
    symbol = "035720"
    
    rows = getHistoricalData(symbol, start, end)
    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                     "Close", "Volume", "Adj Close"])
    
    
    df[['Close']] = df[['Close']].apply(pd.to_numeric)
    closeMax = df['Close'].max()
    closeMin = df['Close'].min()
    
    columns = ['STOCK_CD', 'HIGH', 'LOW', 'STDEV']
    refinedDf = pd.DataFrame(columns=columns)
    refinedDf.loc[0] = [symbol, closeMax, closeMin, 0]
    print refinedDf
