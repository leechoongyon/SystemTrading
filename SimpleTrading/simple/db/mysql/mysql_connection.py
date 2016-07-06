'''
Created on 2016. 6. 30.

@author: lee
'''

import MySQLdb

class MySqlConnection:
    
    def __init__(self, host, user, passwd, db, charset, use_unicode):
        self.conn = MySQLdb.connect(host=host, 
                             user=user, 
                             passwd=passwd, 
                             mysql_conn=db, 
                             charset=charset, 
                             use_unicode=use_unicode)
        
    def getConnection(self):
        return self.conn
    
    def close(self):
        self.conn.close()