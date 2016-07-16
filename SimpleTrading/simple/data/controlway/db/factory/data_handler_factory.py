'''
Created on 2016. 7. 16.

@author: lee
'''
from simple.common.util.properties_util import PropertiesUtil, DB_DATA
from simple.config.configuration import PROPERTIES_PATH
from simple.data.controlway.db.mysql.data_handler import DataHandler


def get_data_handler_in_mysql():
    properties = PropertiesUtil(PROPERTIES_PATH)
    host = properties.config_section_map(DB_DATA)['host']
    user = properties.config_section_map(DB_DATA)['user']
    passwd = properties.config_section_map(DB_DATA)['passwd']
    db = properties.config_section_map(DB_DATA)['db']
    charset = properties.config_section_map(DB_DATA)['charset']
    use_unicode = properties.config_section_map(DB_DATA)['use_unicode']

    data_handler = DataHandler(host, user, passwd, db,\
                                charset, use_unicode)
    
    return data_handler

    
    