'''
Created on 2016. 7. 9.

@author: lee
'''

import pandas as pd
import pandas_datareader.data as web



if __name__ == '__main__':
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    df1 = pd.DataFrame(index=dates)

    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close']
                        , na_values = ['nan'])
    
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    df1 = df1.join(dfSPY, how='inner')
    
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col = 'Date',
                              parse_dates=True, usecols=['Date', 'Adj Close']
                              , na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)
        
    print df1
    
    
    
    '''
    out = web.DataReader("GLD", "yahoo", start_date, end_date)
    out.to_csv('./data/GLD.csv')
    '''
    
