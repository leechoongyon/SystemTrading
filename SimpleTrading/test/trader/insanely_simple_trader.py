# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 14.

@author: lee
'''

import datetime
import time

import schedule

from simple.algorithm import trading_algorithm


def job():
    trading_algorithm.execute()

if __name__ == '__main__':
    
    schedule.every(1).minutes.do(job)
    
    while 1:
        schedule.run_pending()
        time.sleep(1)