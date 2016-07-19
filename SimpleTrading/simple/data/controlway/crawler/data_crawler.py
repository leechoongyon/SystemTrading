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

def get_historical_data(symbol, start, end):
    
    url_string = 'http://www.google.com/finance/historical?q={0}'.format(symbol.upper())
    url_string += "&startdate={0}&enddate={1}d&f=d,o,h,l,c,v&start=0&num=200".format(start, end)
    
    # 번호 뽑아서 그걸로 for문 돌림
    sock = urllib2.urlopen(url_string)
    ch = sock.read()
    sock.close()
    page = re.findall(r"0,\n200,\n[0-9]*", ch)

    
    soup = BeautifulSoup(ch)
    table = soup.find("table", {"class":"gf-table historical_price"})
    ths = table.findAll("th")
    trs = table.findAll("tr")
    print ths
    for tr in trs:
        cols = tr.findAll('td')
        if len(cols) ==0:
            continue
        
#         print "Date : %s " % cols[0].text
#         print "Open : %s " % cols[1].text
#         print "High : %s " % cols[2].text
#         print "Low : %s " % cols[3].text
#         print "Close : %s " % cols[4].text
#         print "Volume : %s " % cols[5].text


    
    # price rows 한 줄씩 뽑기
    
if __name__ == '__main__':
    start = "2014-01-01"
    end = "2016-07-18"
    # kakao = 035720 / combine = 047770
    symbol = "035720"
#     symbol = "047770"
    get_historical_data(symbol, start, end)