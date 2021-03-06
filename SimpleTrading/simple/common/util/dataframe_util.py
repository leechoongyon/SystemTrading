'''
Created on 2016. 7. 16.

@author: lee
'''

import pandas as pd

def readToCsv(path):
    df = pd.read_csv(path)
    return df

def writeToCsv(df, path, fileName):
    df.to_csv(path + "/" + fileName)


def insert(df, idx, col_name, value):
    df.insert(idx, col_name, value)


def rename(df, columns):
    df = df.rename(columns=columns)
    return df

def printAll(df):
    pd.set_option('display.max_rows', len(df))
    print df
    pd.reset_option('display.max_rows')


if __name__ == '__main__':
    raw_data = {'col0': [1, 2, 3, 4, 5],
            'col1': [10, 20, 30, 40, 50],
            'col2': [100, 200, 300, 400, 500]}

    raw_data['score'] = 0
    df = pd.DataFrame(raw_data)
    df.insert(0, 'aaa', 1)
    df.insert(1, 'index', df.index)
    df = rename(df, {"col0":"test","col1":"test1"})
    print df
     