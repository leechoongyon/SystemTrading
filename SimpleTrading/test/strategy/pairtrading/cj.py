# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 19.

@author: lee
'''

import datetime
import math
import time

import numpy as np
import pandas as pd
from simple.common.util.plt_util import plotData
from simple.common.util.stats_util import getData, normalize, normalizeSpread, \
    getLogSpread, getLogSpreadResidual, getCointegrationUsingLog


if __name__ == '__main__':
    two_years_ago = datetime.date.fromtimestamp(time.time() - 730*60*60*24)
    today = datetime.date.fromtimestamp(time.time())
    dates = pd.date_range(two_years_ago, today)
    
    # 0.446616493819, Seafood가 약간 더 고평가네
    symbols = ['CJ_Seafood', 'CJ_CGV']
    
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
    
    
    
    
    
    
    df = getData(symbols, dates)
    refined_df = df.dropna()
    
    # normalize
    normal_df = normalize(symbols, dates, refined_df)
    plotData(normal_df)

    # normalize_spread
    normal_spread_df = normalizeSpread(symbols, normal_df)
    plotData(normal_spread_df)

    # cointegration    
    cointegration = getCointegrationUsingLog(refined_df, symbols)
    print cointegration
    
     # log_spread
    log_spread = getLogSpread(refined_df, cointegration, symbols)
    plotData(log_spread, xlabel="Date", ylabel="log spread")

    # log_spread_residual
    spread_residual = getLogSpreadResidual(refined_df, cointegration, symbols)
    plotData(spread_residual, xlabel="Date", ylabel="Spread_residual")