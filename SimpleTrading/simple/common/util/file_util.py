# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 23.

@author: lee
'''
import os


def mkdir(dirPath):
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

if __name__ == '__main__':
    rawInput = "C:/git/SimpleTrading/SimpleTrading/stock_data/기계/"
    mkdir(rawInput.encode('utf-8'))