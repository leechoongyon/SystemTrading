# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 30.

@author: lee
'''
'''
    num_day는 날짜
    interval_seconds 는 가져오는 분 Interval (301은 5분간격)
'''

from datetime import datetime
import re
import urllib2

from bs4 import BeautifulSoup
import requests

import pandas as pd
from simple.common.util import properties_util, time_util, string_util
from simple.common.util.properties_util import CRAWLER, properties




PAGE_NUM = "page_num"

def get_intraday_data(symbol, interval_seconds=301, num_days=10):
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

def get_total_page_num(symbol, start, end, page_num):
    url_string = 'http://www.google.com/finance/historical?q={0}'.format(symbol.upper())
    url_string += "&startdate={0}&enddate={1}d&f=d,o,h,l,c,v&start=0&num={2}".format(start, end, page_num)
    sock = urllib2.urlopen(url_string)
    ch = sock.read()
    sock.close()
    page = re.findall(r"0,\n" + page_num + ",\n[0-9]*", ch)
    total_num = page[0].replace("\n", "").split(",")[2]
    return total_num

# 다 돌려보고 총 row와 Dataframe 갯수가 맞는지 확인
def get_historical_data(symbol, start, end, page_num, total_page_num):
    
    quotient = total_page_num / page_num
    reminder = total_page_num % page_num
    
    loop_num = 0
    if reminder != 0:
        loop_num = quotient + 1
    else:
        loop_num = quotient
    
    
    rows = []
    for i in range(0, loop_num):
        url_string = 'http://www.google.com/finance/historical?q={0}'.format(symbol.upper())
        url_string += "&startdate={0}&enddate={1}d&f=d,o,h,l,c,v&start={2}&num={3}".format(start, end, page_num * i, page_num)
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
            
            date = time_util.convert_string_to_datetime2(cols[0].text.replace("\n", ""), "%Y-%m-%d")
            open = string_util.multi_replace(cols[1].text, {"\n":"",",":""})
            high = string_util.multi_replace(cols[2].text, {"\n":"",",":""})
            low = string_util.multi_replace(cols[3].text, {"\n":"",",":""})
            close = string_util.multi_replace(cols[4].text, {"\n":"",",":""})
            volume = string_util.multi_replace(cols[5].text, {"\n":"",",":""})
            adj_close = 0
            
            rows.append((date, open, high, \
                        low, close, volume, 0))
            
    
    
    df = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"])
    return df
    
if __name__ == '__main__':
    
    start = "2014-01-01"
    end = "2016-07-22"
    # kakao = 035720 / combine = 047770
    symbol = "035720"
#     symbol = "047770"

    page_num = properties.get_selection(CRAWLER)[PAGE_NUM]
    total_page_num = get_total_page_num(symbol, start, end, page_num)
    print get_historical_data(symbol, start, end, int(page_num), int(total_page_num))    
    