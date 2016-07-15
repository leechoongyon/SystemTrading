# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''
from simple.algorithm import trading_algorithm


 
def before_job():
    print "beforeJob starting"
    
    
def job():
    before_job()
    trading_algorithm.execute()
    after_job()

def after_job():
    print "afterJob starting"
    