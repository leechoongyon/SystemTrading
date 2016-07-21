'''
Created on 2016. 7. 15.

@author: lee
'''
from simple.common.util.properties_util import *
from simple.data.controlway.db.db_data import db_data
import MySQLdb as mdb


def pre_process():
    print "systemPreProcess start" 
    
if __name__ == '__main__':
    properties_path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/stock.properties"
    pre_process(properties_path)