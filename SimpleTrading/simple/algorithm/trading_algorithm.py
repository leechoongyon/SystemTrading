# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 14.

@author: lee
'''

from simple.portfolio import target_portfolio, live_portfolio

def execute():
    print "trading_algorithm executing"
    
    
    '''
        1. CALL TARGET_PORTFOLIO 
         1.1 기본적 분석 + 기술적 분석을 통해 종목 추천
         1.2 추천된 종목을 언제 살지 매수 타이밍을 알아본다.
    '''
    target_portfolio.perform()
    

    '''
        2. CALL LIVE_PORTFOLIO
         2.1 LIVE_PORTFOLIO 에서 주식종목 가져옴
          2.1.1 가져온 종목에 대해서 페어트레이딩 실시
          2.1.2 볼린저 밴드 적용
    '''     
    live_portfolio.perform()