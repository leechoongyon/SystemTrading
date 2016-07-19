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
    
    # 0.446616493819, Seafood가 약간 더 고평가네
#     symbols = ['CJ_Seafood', 'CJ_CGV']2
    
    # 1.20085728854, 스프레드가 거의 비슷
#     symbols = ['CJ_Seafood', 'CJ_Cheiljedang_Wo']
    
    # 1.07068293799 씨푸드가 약간 저평가
#     symbols = ['CJ_Seafood', 'CJ_Cheiljedang']
    
    # 0.288423206405 씨푸드가 고평가
#     symbols = ['CJ_Seafood', 'CJ_HelloVision']

    # 0.403827967574, 잔차 없음
#     symbols = ['CJ_Seafood', 'CJ_KoreaExpress']

    # 0.343803329457, 잔차 거의 없음
#     symbols = ['CJ_Seafood', 'CJ_Seafood_Wo']
    
    # 0.793170891881, 잔차 거의 없음
#     symbols = ['CJ_Seafood', 'CJ']
    
    
    
    
    
    ######################################
    # CJ_Seafood_Wo
    ######################################
    # 1.16907182031, 잔차 거의 없음
#     symbols = ['CJ_Seafood_Wo', 'CJ_CGV']
    
    # 2.62938576394 , 잔차 거의 없음
#     symbols = ['CJ_Seafood_Wo', 'CJ_Cheiljedang_Wo']
    
    
    # 2.64749759518, 잔차 없음
    symbols = ['CJ_Seafood_Wo', 'CJ_Cheiljedang']
    
    
    
    
    
    
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