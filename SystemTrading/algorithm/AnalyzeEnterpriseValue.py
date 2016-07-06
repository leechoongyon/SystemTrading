#-*- coding:utf-8 -*-



'''
Created on 2016. 6. 1.

@author: lee
@Desc : 
   
   기업 가치 분석
1. 사업 가치 평가
  - 영업 이익 평균 (1년별로)
  - Sum = 영업 이익 - (영업이익 * 실효세율) 
  - Sum / 0.06 = 사업 가치 (0.06 은 기대수익율)
2. 재산 가치 평가
  - 유동자산 중의 재산 부분
    유동자산 - 유동부채 * 1.2 = 유동자산
  - 고정자산 중의 재산 부분
    투자자산
  - 유동자산은 예금 (1년 이내에 움직일 수 있는 것)
  - 고정자산은 집 (1년 이내에 움직일 수 없는 것)
  - 재산 가치 = 유동자산 - (유동부채 * 1.2) + 고정자산 중의 투자 자산
3. 부채 빼기
  - 1,2번 에서 구한 
    사업 가치 + 재산 가치 - 부채
4. 발행 주식 수로 나눠 산출


Ex) 팅크웨어

1. 사업 가치
 영업 이익 : 14 + 44 + 31 + 152 / 4
 실효세율 : 16%
 기대수익율 : 6%

2.

113,212,386,339 - (42,842,201,719 * 1.2) = 유동자산 

3. 부채

    - 19,170,264,724

4. 발행 주식 수 : 9,776,005

'''

if __name__ == '__main__':
    # 1. 사업 가치
    avgBizProfit =  (14 + 44 + 31 +152) / 4
    effectiveTaxRates = 0.16
    expectedStockReturns = 0.06
    bizProfit = (avgBizProfit - (avgBizProfit * effectiveTaxRates)) / expectedStockReturns
    print("bizProfit : %s " % bizProfit)