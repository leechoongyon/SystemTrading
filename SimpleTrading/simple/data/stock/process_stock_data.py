# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 18.

@author: lee
'''
from simple.common.util import dataframe_util, string_util
from simple.data.controlway.dataframe.process_dataframe import get_stock_data_using_datareader, \
    register_stock_data_in_db
from simple.data.controlway.db.factory.data_handler_factory import get_data_handler_in_mysql


def get_stock_data(stock_cd, start, end):
    pass

def insert_stock_data():
    pass

# stock_item_daily에 대한 가공
def process_stock_data(df, stock_cd):

    dataframe_util.insert(df, 0, 'STOCK_CD', stock_cd)
    
    indexs = df.index
    indexs = indexs.format()
    indexs = string_util.replace(indexs, "-", "")
    dataframe_util.insert(df, 1, 'YM_DD', indexs)
    columns={"Open":"OPEN_PRICE","High":"HIGH_PRICE", "Low":"LOW_PRICE", "Close":"CLOSE_PRICE", "Adj Close":"ADJ_CLOSE_PRICE"}
    df = dataframe_util.rename(df, columns)
    return df

# stock_item_daily에 대한 가공2 (data_crawler CRAWLER에서 사용)
def process_stock_data2(df, stock_cd):
    dataframe_util.insert(df, 0, 'STOCK_CD', stock_cd)
    columns={"Date":"YM_DD","Open":"OPEN_PRICE","High":"HIGH_PRICE", "Low":"LOW_PRICE", "Close":"CLOSE_PRICE", "Adj Close":"ADJ_CLOSE_PRICE"}
    df = dataframe_util.rename(df, columns)
    return df
    
if __name__ == '__main__':

    # Stock 데이터를 한꺼번에 DB에 밀어넣는다.
    start = "20140101"
    end = "20160718"
    
    # 079160 : CJ CGV /  KaKao : 035720
#     stock_cds = ["079160", "035720"]
#     market_cds = ["KOSPI", "KOSDAQ"]
    stock_cd = "035720"
    market_cd = "KOSDAQ"
    table_nm = "STOCK_ITEM_DAILY"
    exists_option = "append"
    db = "mysql"
    data_handler = get_data_handler_in_mysql()
    con = data_handler.get_conn()
    
    df = get_stock_data_using_datareader(stock_cd, market_cd, start, end)
    df = process_stock_data(df, stock_cd)
    register_stock_data_in_db(con, df, table_nm, exists_option, db)
    
    data_handler.close()
