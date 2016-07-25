'''
Created on 2016. 7. 16.

@author: lee
'''
from simple.common.util.properties_util import PropertiesUtil, DB_DATA, \
    properties
from simple.config.configuration import PROPERTIES_PATH
from simple.data.controlway.db.mysql.data_handler import DataHandler


def getDataHandler():
    host = properties.get_selection(DB_DATA)['host']
    user = properties.get_selection(DB_DATA)['user']
    passwd = properties.get_selection(DB_DATA)['passwd']
    db = properties.get_selection(DB_DATA)['db']
    charset = properties.get_selection(DB_DATA)['charset']
    use_unicode = properties.get_selection(DB_DATA)['use_unicode']

    data_handler = DataHandler(host, user, passwd, db,\
                                charset, use_unicode)
    
    return data_handler

def close(data_handler):
    data_handler.close()
    

    
    