# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 9.

@author: lee
'''

import pandas_datareader.data as web
from simple.common.util.properties_util import PropertiesUtil, STOCK_DATA
from simple.config.configuration import PROPERTIES_PATH


# from simple.trader.trader import properties_path
def get_stock_data(stock_cd, market_cd, start, end):
        
    out = web.DataReader(make_code(stock_cd, market_cd), "yahoo", start, end)
    return out

def regitster_stock_data_in_file(df, stock_nm):
    properties = PropertiesUtil(PROPERTIES_PATH)
    register_path = properties.config_section_map(STOCK_DATA)['stock_download_path']
    df.to_csv(register_path + "/" + stock_nm + ".csv")

def register_stock_data_in_db(data_handler, sql, df):
    pass

def make_code(stock_cd, market_cd):
    if market_cd == "KOSPI": 
        full_stock_cd = "%s.KS" % (stock_cd)
    elif market_cd == "KOSDAQ":
        full_stock_cd = "%s.KQ" % (stock_cd)
    else:
        raise Exception("Not registered market code")
     
    return full_stock_cd
    

if __name__ == '__main__':
    stock_cd = "079160"
    market_cd = "KOSPI"
    start = '20160202'
    end = '20160606'
    print get_stock_data(stock_cd, market_cd, start, end)
#     regitster_stock_data(None, "CJ_CGV")
    '''
    properties_path = "C:/git/SimpleTrading/SimpleTrading/properties/stock.properties"
    properties = PropertiesUtil(properties_path)
    
    stock_download_path = properties.config_section_map(STOCK_DATA)['stock_download_path']
    print stock_download_path
    start = '2009-09-04'
    end = '2016-12-31'
    '''
    
    ######################################################
    # A                                                  #  
    ######################################################
    
    ######################################################
    # B                                                  #  
    ######################################################
    
    ######################################################
    # C                                                  #  
    ######################################################
    
    # CJ CGV (079160)
    '''
    out = web.DataReader("079160.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/CJ_CGV.csv")
    '''

    ######################################################
    # G                                                  #  
    ######################################################

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
    
    ######################################################
    # H                                                  #  
    ######################################################
    
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
    '''
    out = web.DataReader("018880.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/HANRA_GONGJO.csv")
    '''
    
    ######################################################
    # I                                                  #  
    ######################################################
    
    # IBM
    '''
    out = web.DataReader("IBM", "yahoo", start, end)
    out.to_csv('./data/IBM.csv')
    '''
    
    ######################################################
    # M                                                  #  
    ######################################################
    
    # MEIRTZ_FIRE&MARINE_INSURANCE (000060.KS)
    '''
    out = web.DataReader("000060.KS", "yahoo", start, end)
    out.to_csv('./data/MEIRTZ_FIRE&MARINE_INSURANCE.csv')
    '''
    
    # MEIRTZ_FINANCIAL (138040.KS)
    '''
    out = web.DataReader("138040.KS", "yahoo", start, end)
    out.to_csv('./data/MEIRTZ_FINANCIAL.csv')
    '''
    
    # MEIRTZ_SECURITY (008560.KS)
    '''
    out = web.DataReader("008560.KS", "yahoo", start, end)
    out.to_csv('./data/MEIRTZ_SECURITY.csv')
    '''
    
    ######################################################
    # S                                                  #  
    ######################################################
    
    # SAMSUNG_C&T (028260)
    ''' 
    out = web.DataReader("028260.KS", "yahoo", start, end)
    out.to_csv(config.DATA_PATH + "/SAMSUNG_C&T.csv")
    '''
    
    # SAMSUNG (005930)
    
    # SAMSUNG_ABOVE (005935)
    
    # SPY
    '''
    out =  web.DataReader("^GSPC", "yahoo", start, end)
    out.to_csv('./data/SPY.csv')
    '''
    
    ######################################################
    # X                                                  #  
    ######################################################
    
    # XOM
    '''
    out =  web.DataReader("XOM", "yahoo", start, end)
    out.to_csv('./data/XOM.csv')
    '''
    
    
    
    
    
    
    
