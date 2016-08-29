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

from bs4 import BeautifulSoup
import requests

from simple.common.util import regex_util, string_util


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
        row.append(regex_util.sub(old, new, t.text))
        
    
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
    
    
def getBasicStockInfoThroughDaum(stockCd):
    old = "[,%\t\n ]"
    new = ""
    row = []
    dict = {}
    tempRow = []
    url = "http://finance.daum.net/item/quote.daum?code={0}".format(stockCd)
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")
    
    # 종합 주가 정보
    totalStockInfos = soup.find('ul', {'class':'list_descstock'})
    tt = totalStockInfos.find_all('dd')
    for t in tt:
        tempRow.append(regex_util.sub(old, new, t.text))
    
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
    toin = tempRow[8][:toinIndex-1]
    wicsIndex = string_util.searchIndex("\d", tempRow[9])
    wics = tempRow[9][:wicsIndex-1]
    
    # 기본 주가 정보
    stockNm = soup.find('em', {'class':'screen_out'}).text
    basicStockInfos = soup.find('div', {'class':'leftDiv'})
    stockInfos = basicStockInfos.find_all("tr")
    
    row.append(stockCd)
    row.append(stockNm)
    for stockInfo in stockInfos:
        infos = stockInfo.find_all('td', {'class':'num'})
        for info in infos:
            processedData = regex_util.sub(old, new, info.text)
            row.append(processedData)
    
    row.append(eps)
    row.append(per)
    row.append(bps)
    row.append(pbr)
    row.append(toin)
    row.append(wics)
#     row = string_util.convertUnicodeToString(row)
    return row
    
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
            
if __name__ == '__main__':
    
    stockCd = "006360"
#     miniTest(stockCd)
    row = getBasicStockInfoThroughDaum("006360")
    for r in row:
        print r
#     kospiCd = getAllStockCdThroughDaum("kospi")
#     kosdaqCd = getAllStockCdThroughDaum("kosdaq")