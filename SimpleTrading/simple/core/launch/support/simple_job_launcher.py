# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''

import schedule
import time
 
from simple.context import simple_biz_postprocess, simple_biz_preprocess,\
    simple_system_preprocess, simple_system_postprocess
from simple.core.job import simple_job
from simple.common.util.stock_util import check_if_open_market


def run(interval):

    # preProcess
    simple_system_preprocess.pre_process()
    simple_biz_preprocess.pre_process()
    
    # MainService
    schedule.every(interval).minutes.do(simple_job.job)
    
    # 나중에 while문에 특정시간이 됬을 때 종료시키는 로직 추가
    while check_if_open_market():
        schedule.run_pending()
        time.sleep(1)
        
         
    # postProcess
    simple_biz_postprocess.post_process()
    simple_system_postprocess.post_process()
    
if __name__ == '__main__':
    print "simple_job_launcher test"