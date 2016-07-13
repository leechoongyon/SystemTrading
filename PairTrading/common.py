# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 10.

@author: lee
'''
 
import pandas as pd
import matplotlib.pyplot as plt
import os
import config
import math
import numpy as np

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, config.DATA_PATH), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    return df

def get_close_data(symbols, dates):
    """Read stock data (close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, config.DATA_PATH), index_col='Date',
                parse_dates=True, usecols=['Date', 'Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Close': symbol})
        df = df.join(df_temp)

    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def normalize_price(df):
    pass
    
def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    daily_returns = df.copy()
    
    # 1일 앞부터 시작해서 뒤에서 -1까지 해야 수가 같겠지
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    # Note: Returned DataFrame must have the same number of rows
    return daily_returns

def normalize(symbols, dates, df):
    
    # Compute mean, std
    means = {}
    stds = {}
    for symbol in symbols:
        means[symbol] = df[symbol].mean()
        stds[symbol] = df[symbol].std()
        
    # normalize
    normal_df = pd.DataFrame(index=dates)
    
    for symbol in symbols:
        df_temp = (df[symbol] - means[symbol]) / stds[symbol]
        normal_df = normal_df.join(df_temp)
        
    return normal_df


# symbols required argument 2
# 사용법 : symbols 2개가 넘어오고 정규화된 dataFrame이 넘어오면 그것의 values subtract
# 해서 normalize_spread를 만듬
def normalize_spread(symbols, normal_df):
    df_list = []
    for symbol in symbols:
        df_list.append(normal_df[symbol])
    
    normal_spread_df = pd.DataFrame(df_list[0].values - df_list[1].values, index=normal_df.index)
    return normal_spread_df

# 수익률 구하기
def get_earnings_rate(after_stock_price, before_stock_price):
    return math.log(after_stock_price / before_stock_price)


# get_spread_residual
def get_spread_residual(df):
    ln_df = np.log(df).round(2)
    cointegration_coefficient = ln_df.cov()['A']['B'] / ln_df['B'].var()
    log_spread = ln_df['A'] - cointegration_coefficient * ln_df['B']
    log_spread_mean = log_spread.mean()
    spread_residual = log_spread - log_spread_mean
    return spread_residual