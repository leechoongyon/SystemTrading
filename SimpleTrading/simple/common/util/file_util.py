# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 23.

@author: lee
'''
import os
import sys
import time

def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def isFile(path):
    return os.path.isfile(path)

def isDir(path):
    return os.path.isdir(path)

if __name__ == '__main__':
    
    '''
    startNum = int(properties.getSelection(BIZ_PRE_PROCESS)[TARGET_DATA_LOAD_PERIOD])
    start = getDayFromSpecificDay(time.time(), startNum, "%Y%m%d")
    end = getTodayWithFormatting("%Y%m%d")
    path = properties.getSelection(STOCK_DATA)[STOCK_DOWNLOAD_PATH] + "/" + end
    '''
    
    
    raw = "C:/git/SimpleTrading/SimpleTrading/stock_data/018260.csv"
    r = "C:\git\SimpleTrading\SimpleTrading\stock_data\018260.csv"
#     r = r.replace('\/', '/')
    print not isFile(raw)
