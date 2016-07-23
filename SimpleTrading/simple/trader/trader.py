'''
Created on 2016. 7. 15.

@author: lee
'''

from simple.core.launch.support import simple_job_launcher as launcher

class Trader():
    
    def execute(self, interval):
        launcher.run(interval)
        
if __name__ == '__main__':
    interval = 0
    trader = Trader()
    trader.execute(interval)
