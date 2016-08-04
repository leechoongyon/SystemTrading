# -*- coding: utf-8 -*-

'''
Created on 2016. 8. 2.

@author: lee
'''

import time

import pandas as pd
from simple.common.compute_stats import getLogSpreadResidual,\
    getCointegrationUsingLog, getCorrelationCoefficientUsingLog
from simple.common.util.properties_util import properties, BIZ_PRE_PROCESS, \
    TARGET_DATA_LOAD_PERIOD, STOCK_DOWNLOAD_PATH, STOCK_DATA
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting


def applyPairTrading(pairSource, pairTarget, start, end, path):

    statistics = []
    
    # Create refinedDf
    
    stockCds = [pairSource, pairTarget]
    
    dates = pd.date_range(start, end)
    
    df = pd.DataFrame(index=dates)
    sourceDf = pd.read_csv(path + "/" + pairSource + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    targetDf = pd.read_csv(path + "/" + pairTarget + ".csv",
                           index_col = 'Date',
                           parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])
    
    df_temp = sourceDf.rename(columns={'Close': pairSource})
    df = df.join(df_temp)
    df_temp = targetDf.rename(columns={'Close': pairTarget})
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
    
    statistics = [cointegration, residual, correlationCoefficient]
    
    return statistics

if __name__ == '__main__':
    
    '''
            통신업
        017670
        030200
        032640
    '''
    
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]
    print applyPairTrading('017670', '030200', start, end, path)