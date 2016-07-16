'''
Created on 2016. 7. 15.

@author: lee
'''
from simple.common.util.properties_util import *
from simple.data.controlway.db.db_data import db_data
import MySQLdb as mdb


def pre_process(properties_path):
    
    # 1. DB init
    properties = PropertiesUtil(properties_path)
    host = properties.config_section_map(DB_DATA)['host']
    user = properties.config_section_map(DB_DATA)['user']
    passwd = properties.config_section_map(DB_DATA)['passwd']
    db = properties.config_section_map(DB_DATA)['db']
    charset = properties.config_section_map(DB_DATA)['charset']
    use_unicode = properties.config_section_map(DB_DATA)['use_unicode']
    
#     dictCursor = mdb.cursors.DictCursor
#     print dict_cursor
#      if is_dictCursor else None
#     print dict_cursor
    
    db_data.set_data(host, user, passwd, db, charset, use_unicode)
    
    
    
    
    
if __name__ == '__main__':
    properties_path = "C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/stock.properties"
    pre_process(properties_path)