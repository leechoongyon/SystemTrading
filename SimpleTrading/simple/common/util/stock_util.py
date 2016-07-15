'''
Created on 2016. 7. 15.

@author: lee
'''
import datetime

from simple.data.stock.stock_data import stock_data


def check_if_open_market():
    
    dt = datetime.datetime.now()
    curr_time = dt.time()
    return  (stock_data.market_open_time < curr_time) and (curr_time < stock_data.market_close_time) 

    '''
    dt = datetime.datetime.now()
    curr_time = dt.time() 
    start_time =  datetime.time(9,00,0,0)
    end_time = datetime.time(15,30,0,0)
    print curr_time < start_time
    print curr_time < end_time
    
    (start_time < curr_time and curr_time < end_time)
    '''