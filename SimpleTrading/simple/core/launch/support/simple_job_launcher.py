# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import time

import schedule

from simple.common.util.stock_util import checkIfOpenMarket
from simple.context import simple_biz_postprocess, simple_biz_preprocess, \
    simple_system_preprocess, simple_system_postprocess
from simple.core.job import simple_job


def run(interval):

    
    # preProcess
    simple_system_preprocess.preProcess()
    simple_biz_preprocess.preProcess()
     
    # MainService
    schedule.every(interval).minutes.do(simple_job.job)
    
    # 나중에 while문에 특정시간이 됬을 때 종료시키는 로직 추가
    while checkIfOpenMarket():
        schedule.run_pending()
        time.sleep(1)
        
         
    # postProcess 
    simple_biz_postprocess.postProcess()
    simple_system_postprocess.postProcess()
    
if __name__ == '__main__':
    print "simple_job_launcher test"