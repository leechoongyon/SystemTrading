# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 14.

@author: lee
'''

from simple.core.launch.support import simple_job_launcher as launcher



class Trader():
    def __init__(self):
        pass

if __name__ == '__main__':
    
    interval = 1
    launcher.run(interval)