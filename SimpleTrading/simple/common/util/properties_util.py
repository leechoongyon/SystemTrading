# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 15.

@author: lee
'''


import ConfigParser

DB_DATA = "DB_DATA"
STOCK_DATA = "STOCK_DATA"
MARKET_OPEN_TIME = "market_open_time"
MARKET_CLOSE_TIME = "market_close_time"

class PropertiesUtil():
    def __init__(self, filename):
        self.config = ConfigParser.ConfigParser()
        self.config.read(filename)

 
    def config_section_map(self, section):
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



if __name__ == '__main__':
    db_properties = PropertiesUtil("C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/db.properties")
    Name = db_properties.ConfigSectionMap("InsanelySimple")['host']
#     Age = db_properties.ConfigSectionMap("SectionOne")['age']
    print "Hello %s. You are  years old." % (Name)

    '''
    Config = ConfigParser.ConfigParser()
    print Config
    Config.read("C:/Windows/System32/git/SystemTrading/SimpleTrading/properties/db.properties")
    print Config.sections()
    '''
