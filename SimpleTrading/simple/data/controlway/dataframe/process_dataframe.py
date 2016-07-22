# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 9.

@author: lee
'''

import pandas as pd
import pandas_datareader.data as web
from simple.common.util import dataframe_util, string_util
from simple.common.util.properties_util import PropertiesUtil, STOCK_DATA, \
    DB_DATA, properties
from simple.data.controlway.db.factory.data_handler_factory import get_data_handler_in_mysql
from simple.data.controlway.db.mysql.data_handler import DataHandler


# from simple.trader.trader import properties_path
def get_stock_data_using_datareader(stock_cd, market_cd, start, end):
        
    out = web.DataReader(make_code(stock_cd, market_cd), "google", start, end)
    return out

def process_stock_data(df, stock_cd):

    dataframe_util.insert(df, 0, 'STOCK_CD', stock_cd)
    
    indexs = df.index
    indexs = indexs.format()
    indexs = string_util.replace(indexs, "-", "")
    dataframe_util.insert(df, 1, 'YM_DD', indexs)
    columns={"Open":"OPEN_PRICE","High":"HIGH_PRICE", "Low":"LOW_PRICE", "Close":"CLOSE_PRICE", "Adj Close":"ADJ_CLOSE_PRICE"}
    df = dataframe_util.rename(df, columns)
    return df

def regitster_stock_data_in_file(df, stock_nm):
    register_path = properties.get_selection(STOCK_DATA)['stock_download_path']
    df.to_csv(register_path + "/" + stock_nm + ".csv")

'''
    exists_oprtion : append, fail, replace
'''
def register_stock_data_in_db(con, df, table_nm, exists_option, db):
    df.to_sql(con=con, name=table_nm, if_exists=exists_option, flavor=db, index=False)

def make_code(stock_cd, market_cd):
    if market_cd == "KOSPI": 
        full_stock_cd = "%s.KS" % (stock_cd)
    elif market_cd == "KOSDAQ":
        full_stock_cd = "%s.KQ" % (stock_cd)
    else:
        raise Exception("Not registered market code")
     
    return full_stock_cd
    

if __name__ == '__main__':
    
    '''
    raw_data = {'A': [222, 110, 120, 110, 130, 140, 120, 125, 110, 100, 90, 100, 120],
                'B': [300, 320, 350, 330, 370, 390, 380, 385, 365, 300, 310, 270, 310]}
    
    df = pd.DataFrame(raw_data)
    print df
    data_handler = get_data_handler_in_mysql()
    conn = data_handler.get_conn()
    register_stock_data_in_db(conn, df, "test", "append", 'mysql')
#     register_stock_data_in_db(conn, df, STOCK_ITEM_DAILY, 'exists_option', db)
#     regitster_stock_data(None, "CJ_CGV")

    '''
    
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
    
    # 제일제당 우 (097955)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("097955.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_Cheiljedang_Wo.csv')
    '''
    
    # CJ 씨푸드 (011150)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("011150.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_Seafood.csv')
    '''
    
    # CJ 대한통운 (000120)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("000120.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_KoreaExpress.csv')
    '''
    
    # CJ 오쇼핑 (035760)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("035760.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_OShopping.csv')
    '''
    
    # CJ 제일제당 (097950)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("097950.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_Cheiljedang.csv')
    '''
    
    # CJ 씨푸드1우 (011155)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("011155.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_Seafood_Wo.csv')
    '''
    
    # CJ 프레시웨이 (051500)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("051500.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_Freshway.csv')
    '''
    
    # CJ E&M (130960)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("130960.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_E&M.csv')
    '''
    
    # CJ (001040)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("001040.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ.csv')
    '''
    
    # CJ우 (001045)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("001045.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_Wo.csv')
    '''
    
    # CJ헬로비전 (037560)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("037560.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/CJ_HelloVision.csv')
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
    
    
    
    
    
    # Hanwha Investment&Securities Co (003530)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("003530.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/Hanwha_Investment&Securities.csv')
    '''
    
    # Hanwha General Insurance (000370)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("000370.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/Hanwha_General_Insurance.csv')
    '''
    # Hanwha Investment&Securities 우 (003535)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("003535.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/Hanwha Investment&Securities_Wo.csv')
    '''
    
    # 한화에이스스팩2호 (219860)
    # 한화ACPC스팩 (217620)
    
    # Hanwha (000880)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("000880.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/Hanwha.csv')
    '''
    
    # Hanwha Life Insurance Co (088350)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("088350.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/Hanwha_Life_Insurance.csv')
    '''
    
    # 한화우 (000885)
    # 한화에이스스팩1호 (정지)
    # 한화갤러리아타임월드 (027390)
    # 한화MGI스팩 (215380)

    # 한화테크원 (012450)
    '''
    start = '2014-01-01'
    end = '2016-07-19'
    out = web.DataReader("012450.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/Hanwha_Tech.csv')
    '''
    
    # 한화케미칼우 (009835)
    
    
    
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
    
    # MIRAEASSET_DAEWOO (006800)
    '''
    start = '2014-01-01'
    end = '2016-07-22'
    out = web.DataReader("006800.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MIRAEASSET_DAEWOO.csv')
    '''
    
    # MIRAEASSET_LIFE (085620)
    '''
    start = '2015-08-01'
    end = '2016-07-22'
    out = web.DataReader("085620.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MIRAEASSET_LIFE.csv')
    '''
    
    # MIRAEASSET_FINANCE (037620)
    '''
    start = '2014-01-01'
    end = '2016-07-22'
    out = web.DataReader("037620.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MIRAEASSET_FINANCE.csv')
    '''
    
    # MIRAEASSET_DAEWOO_WO (006805)
    '''
    start = '2014-01-01'
    end = '2016-07-22'
    out = web.DataReader("006805.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MIRAEASSET_DAEWOO_WO.csv')
    '''
    
    
    
    
    # MEIRTZ_FIRE&MARINE_INSURANCE (000060.KS)
    
    '''
    start = '2014-01-01'
    end = '2016-07-21'
    out = web.DataReader("000060.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MEIRTZ_FIRE&MARINE_INSURANCE.csv')
    '''
    
    # MEIRTZ_FINANCIAL_GROUP (138040.KS)
    '''
    start = '2014-01-01'
    end = '2016-07-21'
    out = web.DataReader("138040.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MEIRTZ_FINANCIAL_GROUP.csv')
    '''
    # MEIRTZ_SECURITY (008560.KS)
    '''
    start = '2014-01-01'
    end = '2016-07-21'
    out = web.DataReader("008560.KS", "yahoo", start, end)
    out.to_csv('C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/MEIRTZ_SECURITY.csv')
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
    
    
    
    
    
    
    
