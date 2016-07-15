# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 14.

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
#     symbols = ['MEIRTZ_SECURITY', 'MEIRTZ_FINANCIAL']
    symbols = ['MEIRTZ_SECURITY', 'MEIRTZ_FIRE&MARINE_INSURANCE']
    df = get_data(symbols, dates)
    refined_df = df.dropna()
    
    # normalize
    normal_df = normalize(symbols, dates, refined_df)
#     plot_data(normal_df)

    # normalize_spread
    normal_spread_df = normalize_spread(symbols, normal_df)
#     plot_data(normal_spread_df)




    # cointegration    
    cointegration = get_cointegration(refined_df, symbols)
    print cointegration
    
    # log_spread
    log_spread = get_log_spread(refined_df, cointegration, symbols)
#     plot_data(log_spread, xlabel="Date", ylabel="log spread")

    # log_spread_residual
    spread_residual = get_log_spread_residual(refined_df, cointegration, symbols)
    plot_data(spread_residual, xlabel="Date", ylabel="Spread_residual")

