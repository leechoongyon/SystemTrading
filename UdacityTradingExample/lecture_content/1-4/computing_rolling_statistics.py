# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 9.

@author: lee
'''

import os
import pandas as pd
import matplotlib.pyplot as plt

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
    
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    rm_SPY.plot(label="Rolling mean", ax=ax)
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    