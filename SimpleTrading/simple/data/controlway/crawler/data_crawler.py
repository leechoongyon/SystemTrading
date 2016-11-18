# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 30.

@author: lee
'''
from datetime import datetime
import re
import urllib2

from bs4 import BeautifulSoup
import requests

import pandas as pd
from simple.common.util import properties_util, time_util, string_util
from simple.common.util.properties_util import CRAWLER, properties
from simple.data.controlway.dataframe import process_dataframe
from simple.data.controlway.db.factory import data_handler_factory


'''
    num_day는 날짜
    interval_seconds 는 가져오는 분 Interval (301은 5분간격)
'''


PAGE_NUM = "page_num"

def getIntradayData(symbol, interval_seconds=301, num_days=1):
    # Specify URL string based on function inputs.
    url_string = 'http://www.google.com/finance/getprices?q={0}'.format(symbol.upper())
    url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)

    # Request the text, and split by each line
    r = requests.get(url_string).text.split()

    # Split each line by a comma, starting at the 8th line
    r = [line.split(',') for line in r[7:]]

    # Save data in Pandas DataFrame
    df = pd.DataFrame(r, columns=['Datetime','Close','High','Low','Open','Volume'])

    # Convert UNIX to Datetime format
    df['Datetime'] = df['Datetime'].apply(lambda x: datetime.fromtimestamp(int(x[1:])))

    return df

def getTotalPageNum(symbol, start, end, pageNum):
    url_string = 'http://www.google.com/finance/historical?q={0}'.format(symbol.upper())
    url_string += "&startdate={0}&enddate={1}d&f=d,o,h,l,c,v&start=0&num={2}".format(start, end, pageNum)
    sock = urllib2.urlopen(url_string)
    ch = sock.read()
    sock.close()
    page = re.findall(r"0,\n" + str(pageNum) + ",\n[0-9]*", ch)
    total_num = page[0].replace("\n", "").split(",")[2]
    return total_num

def getHistoricalData(stockCd, start, end):
    
    pageNum = int(properties.getSelection(CRAWLER)[PAGE_NUM])
    totalPageNum = int(getTotalPageNum(stockCd,
                                     start, end, pageNum))
    
    quotient = totalPageNum / pageNum
    reminder = totalPageNum % pageNum
    
    loopNum = 0
    if reminder != 0:
        loopNum = quotient + 1
    else:
        loopNum = quotient
    
    
    rows = []
    for i in range(0, loopNum):
        url_string = 'http://www.google.com/finance/historical?q={0}'.format(stockCd.upper())
        url_string += "&startdate={0}&enddate={1}d&f=d,o,h,l,c,v&start={2}&num={3}".format(start, end, pageNum * i, pageNum)
        sock = urllib2.urlopen(url_string)
        ch = sock.read()
        sock.close()
        soup = BeautifulSoup(ch)
        table = soup.find("table", {"class":"gf-table historical_price"})
        trs = table.findAll("tr")
        for tr in trs:
            cols = tr.findAll('td')
            if len(cols) ==0:
                continue
            
            date = time_util.convertStringToDatetime2(cols[0].text.replace("\n", ""), "%Y%m%d")
            open = string_util.multiReplace(cols[1].text, {"\n":"",",":""})
            high = string_util.multiReplace(cols[2].text, {"\n":"",",":""})
            low = string_util.multiReplace(cols[3].text, {"\n":"",",":""})
            close = string_util.multiReplace(cols[4].text, {"\n":"",",":""})
            volume = string_util.multiReplace(cols[5].text, {"\n":"",",":""})
            adj_close = 0
            
            rows.append((date, open, high, \
                        low, close, volume, 0))
    
    # 이렇게 하면 DataFrame으로 리턴
    # df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"])
    # return df
    
    return rows
    
    

if __name__ == '__main__':
    
    start = "2014-01-01"
    end = "2016-07-25"
    # kakao = 035720 / combine = 047770
    symbol = "035720"
#     symbol = "047770"

#     print getIntradayData(symbol)

#     rows = getHistoricalData(symbol, start, end)
#     for row in rows:
#         print row
    
    
    '''
    rows = getHistoricalData(symbol, start, end, int(pageNum), int(totalPageNum))

    dataHandler = data_handler_factory.getDataHandler()
    sql = (
           "INSERT INTO STOCK_ITEM_DAILY " 
                "(STOCK_CD, YM_DD, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, " 
                " CLOSE_PRICE, VOLUME, ADJ_CLOSE_PRICE) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE "
                "YM_DD = VALUES(YM_DD),"
                "OPEN_PRICE = VALUES(OPEN_PRICE), "
                "HIGH_PRICE = VALUES(HIGH_PRICE), "
                "LOW_PRICE = VALUES(LOW_PRICE), "
                "CLOSE_PRICE = VALUES(CLOSE_PRICE), "
                "VOLUME = VALUES(VOLUME), "
                "ADJ_CLOSE_PRICE = VALUES(ADJ_CLOSE_PRICE)"
           )
    
    dataHandler.execSqlManyWithParam(sql, rows)
    '''