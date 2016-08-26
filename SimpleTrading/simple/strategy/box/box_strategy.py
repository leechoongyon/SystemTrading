'''
Created on 2016. 8. 25.

@author: lee
'''

class BoxStrategy():
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def recommend(self):
        
        '''
            1. 2년이내 최저가 근처에 있는지?
             1.1 돌리면 종목들이 나오겠지.
            2. 위에서 추출한 종목들에 대해서 재무재표 적용
             2.1 재무재표로 추출
            3. 위 2가지 필터를 통과한 것을 대상으로 페어 트레이딩 적용
             3.1 Cointegration, 잔차 확인해서 필터링
             3.2 Cointegration은 0.5 이상
             3.3 잔차는 무조건 음수 값 
             3.4 위 2가지 조건을 통과하는 것들을 count 해서 메기기
        '''
        pass

    def applyBox(self):
        
        '''
            1. STOCK_ITEM 전부 돌리기.
             1.1 STOCK_ITEM에서 52주 최저가에 근접하는지 
             1.2 최저가 근접 퍼센트는 옵션으로 제어
        '''
        
        pass
    
    def applyFinancialStandard(self):
        
        '''
            2. 재무 적용
             2.1 PER, PBR 등 적용
        '''
        
        pass


    def applyPairTrading(self):
        pass
    
    
if __name__ == '__main__':
    pass