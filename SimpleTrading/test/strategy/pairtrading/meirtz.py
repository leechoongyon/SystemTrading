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

    # 메리츠 종금증권(MEIRTZ_SECURITY) 을 나머지와 비교
#     symbols = ['MEIRTZ_SECURITY', 'MEIRTZ_FINANCIAL']
#     symbols = ['MEIRTZ_SECURITY', 'MEIRTZ_FIRE&MARINE_INSURANCE']

    # 메리츠 금융지주와(MEIRTZ_FINANCIAL_GROUP) 나머지를 비교
    # 2014-01-01 ~ 2017-07-21 (1.352366989) 한 5프로 저평가
#     symbols = ['MEIRTZ_FINANCIAL_GROUP', 'MEIRTZ_FIRE&MARINE_INSURANCE']

    # 2014-01-01 ~ 2017-07-21 (0.806989394181) 이건 또 고평가네 거의 10%
    symbols = ['MEIRTZ_FINANCIAL_GROUP', 'MEIRTZ_SECURITY']
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

