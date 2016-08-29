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


def getBasicStockInfoThroughDaum(stockCd):
    old = "[,%\t]"
    new = ""
    row = []
    
    url = "http://finance.daum.net/item/quote.daum?code={0}".format(stockCd)
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, "lxml")

    basicStockInfos = soup.find('div', {'class':'leftDiv'})
    stockInfos = basicStockInfos.find_all("tr")
    
    for stockInfo in stockInfos:
        infos = stockInfo.find_all('td', {'class':'num'})
        for info in infos:
            processedData = regex_util.sub(old, new, info.text)
            row.append(string_util.convertUnicodeToString(processedData))
            
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
    row = getBasicStockInfoThroughDaum("006360")
    for obj in row:
        print obj
#     kospiCd = getAllStockCdThroughDaum("kospi")
#     kosdaqCd = getAllStockCdThroughDaum("kosdaq")