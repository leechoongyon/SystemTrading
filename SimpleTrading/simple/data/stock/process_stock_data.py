# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 18.

@author: lee
'''
from simple.data.controlway.dataframe.process_dataframe import get_stock_data_using_datareader, \
    process_stock_data, register_stock_data_in_db
from simple.data.controlway.db.factory.data_handler_factory import get_data_handler_in_mysql


def get_stock_data(stock_cd, start, end):
    pass

def insert_stock_data():
    pass
    
    
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
