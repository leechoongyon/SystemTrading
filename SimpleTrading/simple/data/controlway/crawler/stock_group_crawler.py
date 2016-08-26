'''
Created on 2016. 8. 26.

@author: lee
'''

from bs4 import BeautifulSoup
import requests

def getStockCdUsingGroupCdThroughDaum(groupCd):
    
    stockCds = []
    url = "http://finance.daum.net/quote/group_detail.daum?groupcd={0}".format(groupCd)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    stocks = soup.find_all("dt")
    for stock in stocks:
        tempStock = stock.find('a')
        if tempStock is not None:
            typeConvertStock = str(tempStock)
            index = typeConvertStock.find("code")
            stockCd = typeConvertStock[index + 5: index + 11]
            stockCds.append(stockCd)
            
    return stockCds

def getGroupInfoThroughDaum():
    urls = ["http://finance.daum.net/quote/group.daum?page=1&col=pchgrate&order=desc",
           "http://finance.daum.net/quote/group.daum?page=2&col=pchgrate&order=desc"]
    url = "http://finance.daum.net/quote/group.daum?page=1&col=pchgrate&order=desc"
    
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    tables = soup.findAll("table")
    groups = tables[0].findAll('a')
    
    for group in groups:
        if "groupcd" in group['href']:
            tempGroupCd = str(group['href'])
            groupNm = group.text
            index = tempGroupCd.find('groupcd')
            groupCd = tempGroupCd[index + 8:]
            print groupCd + " / " + groupNm
    
            
    
    '''
    for url in urls:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        soup.findAll("table")
        print soup
    '''
    
if __name__ == '__main__':
#     getGroupInfoThroughDaum()
    stockCds = getStockCdUsingGroupCdThroughDaum("L012")
    