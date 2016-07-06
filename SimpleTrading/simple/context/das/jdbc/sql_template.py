# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 27.

@author: lee
'''

import MySQLdb


class ManagedJdbcTemplate:
    def __init__(self, host, user, passwd, db, charset, use_unicode):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.use_unicode = use_unicode
        
    def selectAll(self, sql):
        db = MySQLdb.connect(host=self.host, 
                             user=self.user, 
                             passwd=self.passwd, 
                             db=self.db, 
                             charset=self.charset, 
                             use_unicode=self.use_unicode)
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return result
        
        
if __name__ == '__main__':
    sql = "SELECT * FROM STOCK_ITEM"
    template = ManagedJdbcTemplate()
    result = template.selectAll(sql)
    
    for StockItem in result:
        print StockItem   