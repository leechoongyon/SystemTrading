# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 30.

@author: lee
'''

from bs4 import BeautifulSoup
import requests

from simple.context.stock.data_model import StockCode


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
    
if __name__ == '__main__':
    
    # 종목 코드 가져오기
    crawler = DataCrawler()
    html = crawler.downloadCode(1)
    codes = crawler.parseCodeHTML(html,1)
    codes.dump()