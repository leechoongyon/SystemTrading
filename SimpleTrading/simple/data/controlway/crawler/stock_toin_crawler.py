'''
Created on 2016. 8. 26.

@author: lee
'''

from bs4 import BeautifulSoup
import requests

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
    plain_text = sourceCode.text
    soup = BeautifulSoup(plain_text, "lxml")
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
    pass
#     kospiCd = getAllStockCdThroughDaum("kospi")
#     kosdaqCd = getAllStockCdThroughDaum("kosdaq")