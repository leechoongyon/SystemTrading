# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 11.

@author: lee
'''

import pandas as pd

from common import get_data, plot_data

if __name__ == '__main__':
    # Read data
    dates = pd.date_range('2010-01-01', '2012-01-31')
    symbol1 = ['HYUNDAI_DEPT']
    symbol2 = ['HYUNDAI_FOOD']
    df1 = get_data(symbol1, dates)
    mean1 = df1.mean()
    std1 = df1.std()
    
    normalization_price1 = (df1 - mean1) / std1  
    
    df2 = get_data(symbol2, dates)
    mean2 = df2.mean()
    std2 = df2.std()
    
    normalization_price2 = (df2 - mean2) / std2

    df = normalization_price1.join(normalization_price2)
    
    plot_data(df)