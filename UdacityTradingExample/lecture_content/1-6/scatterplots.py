# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 10.

@author: lee
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from util import get_data, plot_data, compute_daily_returns


def test_run():
    
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs XOM
    # 기울기와 절편을 구함. 1차함수로  (뒤에 1이 함수 결정)

    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    print "beta_XOM= ", beta_XOM
    print "alpha_XOM= ", alpha_XOM
    plt.plot(daily_returns['SPY'], beta_XOM * daily_returns['SPY'] + alpha_XOM, '-', color='r')
    plt.show()
    
    # Scatterplot SPY vs GLD
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    print "beta GLD= ", beta_GLD
    print "alpha_GLD= ", alpha_GLD
    plt.plot(daily_returns['SPY'], beta_GLD * daily_returns['SPY'] + alpha_GLD, '-', color='r')
    plt.show()
    
    # Calculate correlation coefficient
    print daily_returns.corr(method='pearson')

if __name__ == '__main__':
    test_run()