'''
Created on 2016. 7. 16.

@author: lee
'''
from simple.common.util.properties_util import PropertiesUtil, DB_DATA, \
    properties
from simple.config.configuration import PROPERTIES_PATH
from simple.data.controlway.db.mysql.data_handler import DataHandler


def getDataHandler():
    host = properties.getSelection(DB_DATA)['host']
    user = properties.getSelection(DB_DATA)['user']
    passwd = properties.getSelection(DB_DATA)['passwd']
    db = properties.getSelection(DB_DATA)['db']
    charset = properties.getSelection(DB_DATA)['charset']
    use_unicode = properties.getSelection(DB_DATA)['use_unicode']

    data_handler = DataHandler(host, user, passwd, db,\
                                charset, use_unicode)
    
    return data_handler

def close(data_handler):
    data_handler.close()
    

    
    