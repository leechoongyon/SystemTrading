# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 19.

@author: lee
'''

from simple.strategy.pairtrading.common.pairtrading_common import *

import math
import numpy as np
import time
import datetime



if __name__ == '__main__':
    two_years_ago = datetime.date.fromtimestamp(time.time() - 730*60*60*24)
    today = datetime.date.fromtimestamp(time.time())
    dates = pd.date_range(two_years_ago, today)
    
    
    # 0.202601661191 / 얘도 생명보험이 저평가
    symbols = ['Hanwha_Life_Insurance', 'Hanwha Investment&Securities_Wo']
    
    # -0.171738456361 / 진정한 반비례
#     symbols = ['Hanwha_Life_Insurance', 'Hanwha_General_Insurance']
    
    # 0.277096679487 , 얘는 절반앞에는 반비례인데 뒤에는 비례임. 마찬가지로 생명보험이 저평가
#     symbols = ['Hanwha_Life_Insurance', 'Hanwha_Investment&Securities']
    
    # 0.123523295779 , 그래프가 반비례적인 모양인데? 그리고 생명보험이 전체 그래프가 저점을 찍음
#     symbols = ['Hanwha_Life_Insurance', 'Hanwha'] 
    df = get_data(symbols, dates)
    refined_df = df.dropna()
    
    # normalize
    normal_df = normalize(symbols, dates, refined_df)
    plot_data(normal_df)

    # normalize_spread
    normal_spread_df = normalize_spread(symbols, normal_df)
    plot_data(normal_spread_df)

    # cointegration    
    cointegration = get_cointegration(refined_df, symbols)
    print cointegration
    
     # log_spread
    log_spread = get_log_spread(refined_df, cointegration, symbols)
    plot_data(log_spread, xlabel="Date", ylabel="log spread")

    # log_spread_residual
    spread_residual = get_log_spread_residual(refined_df, cointegration, symbols)
    plot_data(spread_residual, xlabel="Date", ylabel="Spread_residual")