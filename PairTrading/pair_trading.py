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
        2. log_spread
         2.1 A,B 로그 주가 계산
         2.2 두 종목의 Cointegration Coefficient 계산
         2.3 로그 스프레드 계산
         2.4 스프레드 균형점 계산
         2.5 스프레드 잔차 계산
         2.6 차트 그리기
    '''
    
    # 핵심은 0.12 일 때 A를 매도하고 B를 매수하면 향후 스프레드가 낮아질 때 이득이지
    # A에 대해서 B를 평가한거기에 A가 고평가되있을 때 팔고 B가 저평가되있을 때 산다.
    dates = pd.date_range('2010-01-01', '2012-01-31')
    df = pd.read_csv('./data/Sample.csv', index_col='Date', usecols=['Date', 'A', 'B'])
    spread_residual = get_spread_residual(df)
    plot_data(spread_residual)