'''
Created on 2016. 7. 14.

@author: lee
'''

from common import *

import math
import numpy as np


if __name__ == '__main__':
    dates = pd.date_range('2014-01-01', '2016-07-13')
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
    
    cointegration = get_cointegration(refined_df, symbols)
    
    
    # log_spread
    log_spread = get_log_spread(df, cointegration, symbols)
#     plot_data(log_spread, xlabel="Date", ylabel="log spread")
    # log_spread_residual
    spread_residual = get_log_spread_residual(df, cointegration, symbols)
    plot_data(spread_residual, xlabel="Date", ylabel="Spread_residual")
    
    
    # cointegration
#     print 