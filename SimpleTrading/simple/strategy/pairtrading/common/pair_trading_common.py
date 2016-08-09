# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 9.

@author: lee
'''

import pandas as pd
from simple.common.util.stats_util import getCointegrationUsingLog, \
    getCorrelationCoefficientUsingLog, getLogSpreadResidual


def applyPairTrading(pairSourceCode, pairTargetCode, start, end, path):

    statistics = []
    
    # Create refinedDf
    
    stockCds = [pairSourceCode, pairTargetCode]
    
    dates = pd.date_range(start, end)
    
    df = pd.DataFrame(index=dates)
    sourceDf = pd.read_csv(path + "/" + pairSourceCode + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    targetDf = pd.read_csv(path + "/" + pairTargetCode + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    df_temp = sourceDf.rename(columns={'Close': pairSourceCode})
    df = df.join(df_temp)
    df_temp = targetDf.rename(columns={'Close': pairTargetCode})
    df = df.join(df_temp)
    
    refinedDf = df.dropna()
    
    # get cointegration
    cointegration = getCointegrationUsingLog(refinedDf, stockCds)
    
    # get CorrelationCoefficient
    correlationCoefficient = getCorrelationCoefficientUsingLog(refinedDf, stockCds)
    
    # log_spread_residual
    spreadResidual = getLogSpreadResidual(refinedDf, cointegration, stockCds)
#     plotData(spread_residual, xlabel="Date", ylabel="Spread_residual")
#     spreadResidual.sort_index(ascending=False).iloc[0]
    
    # 만약 sort가 필요하면 위에걸 넣고 소트하는데 리소스 소모되니 그냥 찍자    
    residual = spreadResidual.iloc[-1]
    
    statistics = [pairSourceCode, pairTargetCode, cointegration, residual, correlationCoefficient]
    
    return statistics