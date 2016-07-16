# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''


import ConfigParser
from simple.config.configuration import PROPERTIES_PATH

DB_DATA = "DB_DATA"
STOCK_DATA = "STOCK_DATA"

class PropertiesUtil():
    def __init__(self, filename):
        self.config = ConfigParser.ConfigParser()
        self.config.read(filename)
        
 
    def get_selection(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

properties = PropertiesUtil(PROPERTIES_PATH)


if __name__ == '__main__':
    print properties.get_selection("DB_DATA")['host']
#     print properties.config_section_map("DB_DATA")['host']
    
#     db_properties = PropertiesUtil(PROPERTIES_PATH)
#     print db_properties.config_section_map("DB_DATA")['host']
#     Age = db_properties.ConfigSectionMap("SectionOne")['age']
#     print "Hello %s. You are  years old." % (Name)

    '''
    Config = ConfigParser.ConfigParser()
    print Config
    Config.read("C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/db.properties")
    print Config.sections()
    '''
