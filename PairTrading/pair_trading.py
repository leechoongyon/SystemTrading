# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 11.

@author: lee
@desc 

    1. normalize_spread
    2. log_spread
'''

from common import *

if __name__ == '__main__':

    '''
        1. normalize_spread
    '''

    # Read data
    dates = pd.date_range('2010-01-01', '2012-01-31')
    symbols = ['HYUNDAI_DEPT', 'HYUNDAI_FOOD']
    df = get_data(symbols, dates)
    
    # normalize
    normal_df = normalize(symbols, dates, df)
    plot_data(normal_df)
    
    # normalize_spread
    
    normal_spread_df = normalize_spread(symbols, normal_df)
    plot_data(normal_spread_df)
    
    
 
    '''
        2. log_spread
    '''
    