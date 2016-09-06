# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 26.

@author: lee
'''
'''
    기본주가정보
    1. 현재가 / 2. 시가 / 3. 전일비 / 4. 고가 / 5. 등락률
    6. 저가 / 7. 거래량 / 8. 매도 / 9. 거래대금 / 10. 매수
    11. 상한가 / 12. 52주 고가 / 13. 하한가 / 14. 52주 저가 / 15. 연중 최고가
    16. 50일 고가 / 17. 연중 최저가 / 18. 50일 저가 / 19. 시가총액 / 20. 자본금
    21. 상장주식수 / 22. 액면가 / 23. 결산월 / 24. 상장일 / 25. 업종 PER
    26. PER
'''

import sys

from bs4 import BeautifulSoup
import requests

from simple.common.util import string_util
from simple.data.controlway.db.factory import data_handler_factory
from simple.data.stock.query.insert_query import INSERT_STOCK_ITEM_01


def miniTest(stockCd):
    old = "[,%\t\n ]"
    new = ""
    row = []
    url = "http://finance.daum.net/item/quote.daum?code={0}".format(stockCd)
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    totalStockInfos = soup.find('ul', {'class':'list_descstock'})
    tt = totalStockInfos.find_all('dd')
    for t in tt:
        row.append(string_util.sub(old, new, t.text))
        
    
    index = row[5].find('(')
    temps = row[5][:index].split('/')
    print "row[5] : %s " % row[5]
    eps = temps[0]
    per = temps[1]
    
    index = row[7].find('(')
    temps = row[7][:index].split('/')  
    bps = temps[0]
    pbr = temps[1]
    
    toinIndex = string_util.searchIndex("\d", row[8])
    toin = row[8][:toinIndex-1]
    wicsIndex = string_util.searchIndex("\d", row[9])
    wics = row[9][:wicsIndex-1]
    
    print "eps : %s " % eps
    print "per : %s " % per
    
    print "bps : %s " % bps
    print "pbr : %s " % pbr
    
    print "toin : %s " % toin
    print "wics : %s " % wics
    
    
def getBasicStockInfoThroughDaum(stockCd, marketType):
    
    old = "[,%\t\n ]"
    new = ""
    row = []
    tempRow = []
    url = "http://finance.daum.net/item/quote.daum?code={0}".format(stockCd)
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    
    # 종합 주가 정보
    totalStockInfos = soup.find('ul', {'class':'list_descstock'})
    tt = totalStockInfos.find_all('dd')
    for t in tt:
        tempRow.append(string_util.sub(old, new, t.text))
    
    # 5,7,8,9 가 필요한 것
    
    index = tempRow[5].find('(')
    temps = tempRow[5][:index].split('/')
    eps = temps[0]
    per = temps[1]
    
    index = tempRow[7].find('(')
    temps = tempRow[7][:index].split('/')  
    bps = temps[0]
    pbr = temps[1]
    
    toinIndex = string_util.searchIndex("\d", tempRow[8])
    toin = ""
    if toinIndex is not None:
        toin = tempRow[8][:toinIndex-1]
    else:
        toin = ""
        
    wicsIndex = string_util.searchIndex("\d", tempRow[9])
    wics = ""
    if wicsIndex is not None:
        wics = tempRow[9][:wicsIndex-1]
    else:
        wics = ""
    
    # 기본 주가 정보
#     stockNm = soup.find('em', {'class':'screen_out'}).text
    stockNmItem = soup.find('div', {'class':'topInfo'})
    stockNm = stockNmItem.find('h2').text
    
    
    basicStockInfos = soup.find('div', {'class':'leftDiv'})
    stockInfos = basicStockInfos.find_all("tr")
    
    row.append(stockCd)
    row.append(stockNm)
    for stockInfo in stockInfos:
        infos = stockInfo.find_all('td', {'class':'num'})
        for info in infos:
            processedData = string_util.sub(old, new, info.text)
            row.append(processedData)
    
    row.append(eps)
    row.append(per)
    row.append(bps)
    row.append(pbr)
    row.append(toin)
    row.append(wics)
    row.append(marketType)
    return row
    
def getFinancialStockInfoThroughDaum(stockCd):
    
    url = "http://wisefn.stock.daum.net/company/c1030001_1.aspx?cmp_cd=088350"
#     url = "http://finance.daum.net/item/company.daum?code=088350&type=11"
#     url = "http://finance.daum.net/item/company.daum?code={0}&type=11".format(stockCd)
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    
    print soup

def getAllStockCdThroughDaum(marketNm):
    
    url = ""
    if marketNm == "kospi":
        url = "http://finance.daum.net/quote/all.daum?type=U&stype=P"
    elif marketNm == "kosdaq":
        url = "http://finance.daum.net/quote/all.daum?type=U&stype=Q"
    else:
        print "ERROR invalid marketNm : %s" , marketNm
    
    
    stockCds = []
    
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    toins = soup.find_all("table", {"class":"gTable clr"})
    
    for toin in toins:
        stockItems = toin.find_all("a")
        for stockItem in stockItems:
            tempStockItem = str(stockItem)
            index = tempStockItem.find("code")
            stockCd = tempStockItem[index + 5: index + 11]
            stockCds.append(stockCd)
            
    return stockCds

def processStockData(tempRows):

    '''
        저장할 목록
        0. 종목코드 (0) / 1. 종목명(1) / 2. 현재가(2) / 3. 52주 고가(13)
        4. 52주 저가 (15) / 5. EPS(28) / 6. BPS(30) / 7. PER(29)
        8. PBR(31) / 9. TOIN(32) / 10. TOIN_PER(26)
        11. WICS(33) / 12. 시가총액(20)
    '''
    
    rows = []
    for tempRow in tempRows:
        row = [tempRow[0], tempRow[1], tempRow[2], tempRow[13],
               tempRow[15], tempRow[28], tempRow[30], tempRow[29],
               tempRow[31], tempRow[32], tempRow[26], tempRow[33],
               tempRow[20]]
        realRow = convertStockType(row)
        rows.append(realRow)
        
    return rows
            
            
def convertStockType(rows):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    realRow = []
    index = 0
    print rows
    for row in rows:
        tempRow = str(unicode(row))
        
        if index == 2:
            if tempRow is '':
                tempRow = 0
            else:
                tempRow = int(tempRow)
        elif index == 3:
            if tempRow is '':
                tempRow = 0
            else:
                tempRow= int(tempRow)
        elif index == 4:
            if tempRow is '':
                tempRow = 0
            else:
                tempRow = int(tempRow)
        elif index == 5 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)    
        elif index == 6 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 7 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 8 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 10 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        elif index == 12 :
            if tempRow is '':
                tempRow = 0.0
            else:
                tempRow = float(tempRow)
        
        index += 1    
        realRow.append(tempRow)
        
    return realRow

def storeBasicStockInfoInDB(rows):
    dataHandler = data_handler_factory.getDataHandler()
    dataHandler.execSqlManyWithParam(INSERT_STOCK_ITEM_01,
                                           rows)

    data_handler_factory.close(dataHandler)



if __name__ == '__main__':
    
    stockCd = "000075"
    miniTest(stockCd)
    rows = []

#     row = getBasicStockInfoThroughDaum(stockCd)
#     rows.append(row)
#     realRows = processStockData(rows)
#     print "realRows : %s " % realRows
#     storeBasicStockInfoInDB(realRows)            
    
#     kospiCd = getAllStockCdThroughDaum("kospi")
#     kosdaqCd = getAllStockCdThroughDaum("kosdaq")