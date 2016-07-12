# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 9.

@author: lee
'''

import pandas_datareader.data as web
import config

if __name__ == '__main__':
    
    start = '2009-09-04'
    end = '2012-01-30'
    
    # HYUNDAI_DEPT (069960)
    '''
    out = web.DataReader("069960.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/HYUNDAI_DEPT.csv")
    '''
    # HYUNDAI_FOOD (005440)
    '''
    out = web.DataReader("005440.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/HYUNDAI_FOOD.csv")
    '''
    
    # HYUNDAI_MOBIS (012330)
    '''
    out = web.DataReader("012330.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/HYUNDAI_MOBIS.csv")
    '''
    
    # HANRA_GONGJO (018880)
    out = web.DataReader("018880.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/HANRA_GONGJO.csv")
    
    
    # SAMSUNG (005930)
    
    # SAMSUNG_ABOVE (005935)
    
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
