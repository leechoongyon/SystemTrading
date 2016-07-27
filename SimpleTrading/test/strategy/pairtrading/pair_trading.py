# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 26.

@author: lee
'''
import datetime
import time

import pandas as pd
from simple.common.util.properties_util import properties, CRAWLER, STOCK_DATA, \
    STOCK_DOWNLOAD_PATH
from simple.common.util.time_util import getDayFromSpecificDay, \
    getTodayWithFormatting
from simple.data.controlway.crawler import data_crawler
from simple.data.controlway.crawler.data_crawler import PAGE_NUM
from simple.data.stock.stock_data import StockColumn
from simple.strategy.pairtrading.common.pairtrading_common import symbolToPath, \
    normalize, getCointegration, getLogSpread, getLogSpreadResidual, plotData, \
    normalizeSpread


if __name__ == '__main__':
    
    # 코드 2개를 입력받아 2년치 데이터를 가져와서 파일로 만들기
    # 035720 : KaKao, 079160 : CJ CGV
    # 0. 초기 세팅 (stockCds에 2개만 넣어주면 작동
    stockCds = ["035720", "079160"]
    
    
    startNum = -730
    start = getDayFromSpecificDay(time.time(), int(startNum), "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    two_years_ago = datetime.date.fromtimestamp(time.time() - 730*60*60*24)
    today = datetime.date.fromtimestamp(time.time())
    dates = pd.date_range(two_years_ago, today)

    # 1. StockData 파일 만들기
    for stockCd in stockCds:    
        pageNum = properties.getSelection(CRAWLER)[PAGE_NUM]
        totalPageNum = data_crawler.getTotalPageNum(stockCd,
                                         start, end, pageNum)
        rows = data_crawler.getHistoricalData1(stockCd, start, end, 
                                              int(pageNum), 
                                              int(totalPageNum))
        df = pd.DataFrame(rows, columns=["Date", "Open", "High", 
                                         "Low", "Close", "Volume", 
                                         "Adj Close"])
        df.to_csv(properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH]
                    + "/" + stockCd + ".csv", index=False)
    
    # 1. csv 읽어들여 DataFrame으로 만들기 (예시 참고해서 그대로 사용)
    df = pd.DataFrame(index=dates)
    for stockCd in stockCds:
        df_temp = pd.read_csv(symbolToPath(stockCd, 
                              properties.getSelection(STOCK_DATA)['stock_download_path']), 
                              index_col='Date',
                              parse_dates=True, usecols=['Date', 'Close'], 
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Close': stockCd})
        df = df.join(df_temp)
#     df = getData(stockCds, dates)
    refinedDf = df.dropna()
    
    
    
    
    # 2. 계산
    # normalize
    normal_df = normalize(stockCds, dates, refinedDf)
    plotData(normal_df)

    # normalize_spread
    normal_spread_df = normalizeSpread(stockCds, normal_df)
    plotData(normal_spread_df)

    # cointegration    
    cointegration = getCointegration(refinedDf, stockCds)
    print cointegration
    
     # log_spread
    log_spread = getLogSpread(refinedDf, cointegration, stockCds)
    plotData(log_spread, xlabel="Date", ylabel="log spread")

    # log_spread_residual
    spread_residual = getLogSpreadResidual(refinedDf, cointegration, stockCds)
    plotData(spread_residual, xlabel="Date", ylabel="Spread_residual")