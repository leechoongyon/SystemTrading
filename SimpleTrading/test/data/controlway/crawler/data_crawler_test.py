# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 29.

@author: lee
'''
import os

from bs4 import BeautifulSoup
import requests

import pandas as pd
from simple.common.util import file_util, string_util
from simple.common.util.properties_util import properties, STOCK_DATA
from simple.data.controlway.crawler.data_crawler import getHistoricalData


def getBasicStockInfoThroughDaum(stockCd):
    
    old = "[,%\t\n ]"
    new = ""
    row = []
    tempRow = []
    url = "http://finance.daum.net/item/quote.daum?code={0}".format(stockCd)
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    
    # 기본 주가 정보
    stockNm = soup.find('div', {'class':'topInfo'})
    print stockNm.find('h2').text

if __name__ == '__main__':
    start = "2014-01-01"
    end = "2016-07-25"
    # kakao = 035720 / combine = 047770
    symbol = "000070"
 
    getBasicStockInfoThroughDaum(symbol)
 
    '''
        
    '''
 
 
 
    '''
    # history를 읽어서 df에 담기   
    rows = getHistoricalData(symbol, start, end)
    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                     "Close", "Volume", "Adj Close"])
    
    df[['Close']] = df[['Close']].apply(pd.to_numeric)
    closeMax = df['Close'].max()
    closeMin = df['Close'].min()
    
    columns = ['STOCK_CD', 'HIGH', 'LOW', 'STDEV']
    refinedDf = pd.DataFrame(columns=columns)
    refinedDf.loc[0] = [symbol, closeMax, closeMin, 0]
    print refinedDf
    '''
    
    '''
    rows = getHistoricalData(symbol, start, end)
    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", 
                                     "Close", "Volume", "Adj Close"])
    path = properties.getSelection(STOCK_DATA)['stock_download_path']
#     df.to_csv(path + "/기계/" + symbol + ".csv", index=False)
    rPath = "C:/git/SimpleTrading/SimpleTrading/stock_data/기계/"
    file_util.mkdir(rPath)
    df.to_csv(os.path.join(path, "/기계/035720.csv"), index=False)
    df = pd.read_csv(path + "/기계/" + symbol + ".csv")
    print df
    '''