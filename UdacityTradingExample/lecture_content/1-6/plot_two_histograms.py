'''
Created on 2016. 7. 10.

@author: lee
'''

import pandas as pd
import matplotlib.pyplot as plt

from common import get_data, plot_data, compute_daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
#     plot_data(daily_returns, title="Daily returns")

    # Plot histogram directly from dataframe
    daily_returns['SPY'].hist(bins=20, label="SPY")
    daily_returns['XOM'].hist(bins=20, label="XOM")
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    test_run()