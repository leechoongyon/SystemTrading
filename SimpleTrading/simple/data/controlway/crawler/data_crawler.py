# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 30.

@author: lee
'''

from datetime import datetime

import requests

import pandas as pd


'''
    num_day는 날짜
    interval_seconds 는 가져오는 분 Interval (301은 5분간격)
'''

def get_intraday_data(symbol, interval_seconds=301, num_days=10):
    # Specify URL string based on function inputs.
    url_string = 'http://www.google.com/finance/getprices?q={0}'.format(symbol.upper())
    url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)

    print url_string

    # Request the text, and split by each line
    r = requests.get(url_string).text.split()

    # Split each line by a comma, starting at the 8th line
    r = [line.split(',') for line in r[7:]]

    # Save data in Pandas DataFrame
    df = pd.DataFrame(r, columns=['Datetime','Close','High','Low','Open','Volume'])

    # Convert UNIX to Datetime format
    df['Datetime'] = df['Datetime'].apply(lambda x: datetime.fromtimestamp(int(x[1:])))

    return df


'''
class DataCrawler():
    
    def __init__(self):
        pass
    
    def downloadCode(self,market_type):
        url = 'http://datamall.koscom.co.kr/servlet/infoService/SearchIssue'
        html = requests.post(url, data={'flag':'SEARCH', 'marketDisabled': 'null', 'marketBit':market_type})
        return html.content
    
    def parseCodeHTML(self,html,market_type):
        soup = BeautifulSoup(html)
        options = soup.findAll('option')
        
        codes = StockCode()
        
        for a_option in options:
            #print a_tr
            if len(a_option)==0:
                continue

            code = a_option.text[1:7] 
            company = a_option.text[8:]
            full_code = a_option.get('value')
            
            
            codes.add(market_type,code,full_code,company)

        return codes
'''

if __name__ == '__main__':
    
    
    print get_intraday_data("035720.KQ")
    
    # 종목 코드 가져오기
    '''
    crawler = DataCrawler()
    html = crawler.downloadCode(1)
    codes = crawler.parseCodeHTML(html,1)
    codes.dump()
    '''