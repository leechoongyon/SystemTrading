# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 19:25:07 2014

@author: francesco
"""
import pandas as pd
import Quandl 
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt


if __name__ == '__main__':
    start = datetime.datetime(1990, 1, 1)
    end = datetime.datetime(2014, 8, 31)
    path = './datasets/'

    '''
    ## APPLE 
    out = web.DataReader("AA", "yahoo", start, end)
#     out =  web.get_data_yahoo('AA', start, end)

    out.columns.values[-1] = 'AdjClose'
    out.columns = out.columns + '_Out'
    out['Return_Out'] = out['AdjClose_Out'].pct_change()
    
    out.to_csv('./datasets/alcoa.csv')
    print out
    
    '''
    
    '''
    ### S&P - 500 ^GSPC Yahoo Finance
    sp =  web.DataReader("^GSPC", "yahoo", start, end)
    sp.columns.values[-1] = 'AdjClose'
    sp.columns = sp.columns + '_SP500'
    sp['Return_SP500'] = sp['AdjClose_SP500'].pct_change()
    sp.to_csv('./datasets/sp500.csv')

    plt.plot(sp['AdjClose_SP500'])
    plt.legend(('Dividend Adjusted Close Price S&P-500',))
    plt.show()
    '''
    
    '''
### Nasdaq Composite ^IXIC Yahoo Finance
    nasdaq =  web.DataReader('^IXIC', 'yahoo', start, end)

    nasdaq.columns.values[-1] = 'AdjClose'
    nasdaq.columns = nasdaq.columns + '_Nasdaq'
    nasdaq['Return_Nasdaq'] = nasdaq['AdjClose_Nasdaq'].pct_change()
    nasdaq.to_csv('./datasets/nasdaq.csv')
    '''
    
    '''
### Dow Jones Industrial Average (YFinance - Quandl)
    djia = Quandl.get("YAHOO/INDEX_DJI", trim_start='1990-01-01', trim_end='2014-08-31', authtoken="mCDHcSdN9mQ_Hubid1Uq")

    djia.columns.values[-1] = 'AdjClose'
    djia.columns = djia.columns + '_Djia'
    djia['Return_Djia'] = djia['AdjClose_Djia'].pct_change()

    djia.to_csv('./datasets/djia.csv')
    '''
    
    '''
### 5 Years US Treasury YTM ^FVX Yahoo Finance
    treasury = web.DataReader('^FVX', 'yahoo', start, end)
    treasury.columns.values[-1] = 'AdjClose'
    treasury.columns = treasury.columns + '_Treasury'
    treasury['Return_Treasury'] = treasury['AdjClose_Treasury'].pct_change()
    treasury.to_csv('./datasets/treasury.csv')
    '''

    '''
### Hong Kong Hang Seng ^HSI Yahoo Finance
    hkong =  web.DataReader('^HSI', 'yahoo', start, end)
    hkong.columns.values[-1] = 'AdjClose'
    hkong.columns = hkong.columns + '_HKong'
    hkong['Return_HKong'] = hkong['AdjClose_HKong'].pct_change()
    hkong.to_csv('./datasets/hkong.csv')
    '''
    
    '''
### Frankfurt DAX ^GDAXI Yahoo Finance
    frankfurt =  web.DataReader('^GDAXI', 'yahoo', start, end)
    frankfurt.tail()
    frankfurt.columns.values[-1] = 'AdjClose'
    frankfurt.columns = frankfurt.columns + '_Frankfurt'
    frankfurt['Return_Frankfurt'] = frankfurt['AdjClose_Frankfurt'].pct_change()
    frankfurt.to_csv('./datasets/frankfurt.csv')
    '''

    '''
### Paris CAC 40 ^FCHI Yahoo Finance
    paris =  web.DataReader('^FCHI', 'yahoo', start, end)
    paris.columns.values[-1] = 'AdjClose'
    paris.columns = paris.columns + '_Paris'
    paris['Return_Paris'] = paris['AdjClose_Paris'].pct_change()
    paris.to_csv('./datasets/paris.csv')
    '''

    '''
### Tokyo Nikkei-225 ^N225 Yahoo Finance
    nikkei =  web.DataReader('^N225', 'yahoo', start, end)
    nikkei.columns.values[-1] = 'AdjClose'
    nikkei.columns = nikkei.columns + '_Nikkei'
    nikkei['Return_Nikkei'] = nikkei['AdjClose_Nikkei'].pct_change()
    nikkei.to_csv('./datasets/nikkei.csv')
    '''

    '''
### London FTSE-100 ^FTSE Yahoo Finance 
    london = web.DataReader('^FTSE', 'yahoo', start, end)
    london.columns.values[-1] = 'AdjClose'
    london.columns = london.columns + '_London'
    london['Return_London'] = london['AdjClose_London'].pct_change()
    london.to_csv('./datasets/london.csv')
    '''

    '''
### Australia ASX-200 ^AXJO Yahoo Finance
    australia = web.DataReader('^AXJO', 'yahoo', start, end)
    australia.columns.values[-1] = 'AdjClose'
    australia.columns = australia.columns + '_Australia'
    australia['Return_Australia'] = australia['AdjClose_Australia'].pct_change()
    australia.to_csv('./datasets/australia.csv')
    '''

    '''
########### RAW MATERIALS AND CURRENCIES
### Oil Price US Department for Energy (Quandl)
    oil =  Quandl.get("DOE/RWTC", trim_start='2008-01-01', trim_end='2014-08-15', authtoken="mCDHcSdN9mQ_Hubid1Uq")
    oil.columns = oil.columns + '_Oil'
    oil['Delta_Oil'] = oil['Value_Oil'].pct_change()
    '''

### Gold Price (Bundesbank - Quandl)
#gold = Quandl.get("BUNDESBANK/BBK01_WT5511", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#gold.columns = gold.columns + '_Gold'
#gold['Delta_Gold'] = gold['Value_Gold'].pct_change()
#
### Dollar in Euros Rate Exchange
#euro = Quandl.get("QUANDL/EURUSD", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#euro.columns = euro.columns + '_Euro'
#euro['Delta_Euro'] = euro['Rate_Euro'].pct_change()
#
### Dollar in Japanese Yen Rate Exchange
#yen = Quandl.get("QUANDL/USDJPY", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#yen.columns = yen.columns + '_Yen'
#yen['Delta_Yen'] = yen['Rate_Yen'].pct_change()
#
### Dollar in Australian Dollars Rate Exchange
#aud = Quandl.get("QUANDL/USDAUD", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#aud.columns = aud.columns + '_Aud'
#aud['Delta_Aud'] = aud['Rate_Aud'].pct_change()
