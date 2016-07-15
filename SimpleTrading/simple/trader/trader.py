'''
Created on 2016. 7. 15.

@author: lee
'''

from simple.core.launch.support import simple_job_launcher as launcher

properties_path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/stock.properties"

class Trader():
    
    def execute(self, interval, properties_path):
        launcher.run(interval, properties_path)
        
if __name__ == '__main__':
    interval = 0
    trader = Trader()
    trader.execute(interval, properties_path)