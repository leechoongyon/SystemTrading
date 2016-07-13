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
    refined_df = df.dropna()
    # normalize
    normal_df = normalize(symbols, dates, refined_df)
    plot_data(normal_df)
    
    # normalize_spread
    
    normal_spread_df = normalize_spread(symbols, normal_df)
    plot_data(normal_spread_df)
    '''
 
 
    '''
            핵심은 0.12 일 때 A를 매도하고 B를 매수하면 향후 스프레드가 낮아질 때 이득이지
        A에 대해서 B를 평가한거기에 A가 고평가되있을 때 팔고 B가 저평가되있을 때 산다.
            아래 Cointegration 계수는 종목 B의 계수를 구하는 것이다.
        B의 계수 = A와 B의 공분산 / B의 분산
            종목 A에 대한 종목 B의 상대적 베타 계수
            
            주의점은 주가 분포가 어느정도 유사해야 이 계수가 1에 가깝게 나온다.  
    '''
    dates = pd.date_range('2010-01-01', '2012-01-31')
    df = pd.read_csv('./data/Sample.csv', index_col='Date', usecols=['Date', 'A', 'B'])
    spread_residual = get_spread_residual(df)
    plot_data(spread_residual, xlabel="Date", ylabel="Spread_residual")