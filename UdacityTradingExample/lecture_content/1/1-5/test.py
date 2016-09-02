'''
Created on 2016. 8. 27.

@author: lee
'''

import pandas_datareader.data as web
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
#     if 'SPY' not in symbols:  # add SPY for reference, if absent
#         symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv("C:/git/SimpleTrading/UdacityTradingExample/data/GOOG.csv", index_col='Date',
                    parse_dates=True, usecols=['Date', 'Adj Close']
                    , na_values=['nan'])
        
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp, how='inner')
        
    return df

def plot(df_data):
    ax = df_data.plot(title="Incomplete Data", fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()    

if __name__ == '__main__':
    symbols = ["FAKE2"]
    start_date = "2010-01-01"
    end_date = "2016-07-15"
    idx = pd.date_range(start_date, end_date)
    df = get_data(symbols, idx)
    print df
    plot(df) 
