'''
Created on 2016. 7. 15.

@author: lee
'''

import schedule
import time

from simple.core.job import simple_job


def job():
    print "job"

def run(interval):
    
    schedule.every(interval).minutes.do(simple_job.job)
    
    while 1:
        schedule.run_pending()
        time.sleep(1)