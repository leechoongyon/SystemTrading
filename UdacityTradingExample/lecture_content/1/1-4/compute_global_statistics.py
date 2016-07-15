# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 9.

@author: lee
'''

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol, "C:/git/SimpleTrading/UdacityTradingExample/data"), index_col='Date',
                    parse_dates=True, usecols=['Date', 'Adj Close']
                    , na_values=['nan'])
        
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp, how='inner')
        
    
    return df


if __name__ == '__main__':
    
    dates = pd.date_range('2010-01-01', '2010-12-31')
    symbols = ['GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
    print df.mean()
    print df.std()
    