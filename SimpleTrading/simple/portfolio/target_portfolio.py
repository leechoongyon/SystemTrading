# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
from simple.strategy.pairtrading import pairtrading


def preProcess():
    pass

def postProcess():
    pass

def perform():

    preProcess()
    
    '''
        1. TARGET_PORTFOLIO 
         1.1 추천된 종목을 언제 살지 매수 타이밍을 알아본다.
          1.1.1 타겟포트폴리오 종목 가져오기
          1.1.2 해당 종목 현재가 가져오기
          1.1.3 그 종목의 볼린저밴드, 기타 등등 비교
    '''
    
    # 여기엔 전략의 Buy 가 오면 됨.
    pairtrading.buy()
    
    
    
        
    postProcess()
    
    
def selectionOfStockItems():
    
    # 각 전력의 Recommend 가 여기에 위치
    recommendDf = pairtrading.recommend()
    
    
if __name__ == '__main__':
    print selectionOfStockItems()
#     perform()    