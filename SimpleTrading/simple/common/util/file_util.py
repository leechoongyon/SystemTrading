# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 23.

@author: lee
'''
import os
import sys

def mkdir(dirPath):
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

if __name__ == '__main__':
    
    rawInput = "C:/Windows/System32/git/SystemTrading/SimpleTrading/stock_data/machine"
    
    mkdir(rawInput)
