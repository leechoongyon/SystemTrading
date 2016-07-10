'''
Created on 2016. 7. 9.

@author: lee
'''

import pandas_datareader.data as web

if __name__ == '__main__':
    
    start = '2010-01-01'
    end = '2016-12-31'
    
    # SPY
    '''
    out =  web.DataReader("^GSPC", "yahoo", start, end)
    out.to_csv('./data/SPY.csv')
    '''
    
    # XOM
    '''
    out =  web.DataReader("XOM", "yahoo", start, end)
    out.to_csv('./data/XOM.csv')
    '''
    
    # GLD
    '''
    out = web.DataReader("GLD", "yahoo", start, end)
    out.to_csv('./data/GLD.csv')
    '''
    
    # GOOG
    '''
    out = web.DataReader("GOOG", "yahoo", start, end)
    out.to_csv('./data/GOOG.csv')
    '''
    # IBM
    '''
    out = web.DataReader("IBM", "yahoo", start, end)
    out.to_csv('./data/IBM.csv')
    '''
