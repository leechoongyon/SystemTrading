# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 29.

@author: lee
'''
import json
import os
import re
import urllib2

from bs4 import BeautifulSoup
import requests
from simple.common.util import string_util


def getFinancialStockInfoThroughDaum(stockCd):

    dict = {}

    url = "http://wisefn.stock.daum.net/company/cF1001.aspx?cmp_cd=005380&finGubun=MAIN"
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    script = soup.find(lang="javascript")
    
    '''
    # json 됨
    js = json.loads(script.string.split(";")[0].split(" = ")[1])
    print js
    '''
    
    rawData = script.string.split(";")[0].split(" = ")[1]
    old = "[연결\<\>brspan class\(\)IFRS\/mutiow\\'vhge\=\-\;]"
    new = ""
    dates = string_util.sub(old, new, rawData)
    dates = string_util.convertUnicodeToString(dates)
    jsDate = json.loads(dates)
    dict['date'] = jsDate

    rawData = script.string.split(";")[1].split(" = ")[1]
    jsStats = json.loads(rawData)
    dict['stats'] = jsStats
    
    return dict
    
    '''
    old = "[\<\>brspan class\(\)IFRS연결\/mutiow\"\'vhge\=\-\;]"
    new = ""
    url = "http://wisefn.stock.daum.net/company/cF1001.aspx?cmp_cd={0}&finGubun=MAIN".format(stockCd)
    for line in urllib2.urlopen(url):
        if "changeFin " in line:
            data = string_util.sub(old, new, line)
            processedData = json.loads(data)
            print processedData
    
        if "changeFinData" in line:
    '''     
    
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
    
    '''
    start = "2014-01-01"
    end = "2016-07-25"
    # kakao = 035720 / combine = 047770
    symbol = "000070"
    getBasicStockInfoThroughDaum(symbol)
    '''
 
    stockCd = "000070"
    dict = getFinancialStockInfoThroughDaum(stockCd)
#     print dict['date']
    print dict['stats'][0][0][0]
    print dict['stats'][0][0]
    
    