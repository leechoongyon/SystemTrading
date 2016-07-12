# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 11.

@author: lee
@desc 

    1. normalize_spread
    2. log_spread
'''

from common import *

import math
import numpy as np

if __name__ == '__main__':

    '''
        1. normalize_spread
    '''

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
    
 
    '''
        2. log_spread
         2.1 A,B 로그 주가 계산
         2.2 두 종목의 Cointegration Coefficient 계산
         2.3 로그 스프레드 계산
         2.4 스프레드 균형점 계산
         2.5 스프레드 잔차 계산
         2.6 차트 그리기
    '''
    
    # Read data
    dates = pd.date_range('2010-01-01', '2012-01-31')
    symbols = ['SAMSUNG', 'SAMSUNG_ABOVE']
    df = get_data(symbols, dates)
    ln_df = np.log(df)
    cov_df = ln_df.cov()
    print cov_df['HYUNDAI_DEPT']['HYUNDAI_FOOD']
    
    
