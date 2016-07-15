# -*- coding: utf-8 -*-

'''
Created on 2016. 6. 30.

@author: lee
'''
import MySQLdb


class ConnectionFactory:
    
    conn = MySQLdb
    
    def __init__(self, host, user, passwd, db, charset, use_unicode):
        
        # 추후 다른 DB가 생기면 추가    
        self.conn = MySQLdb.connect(host=host, 
                           user=user, 
                           passwd=passwd, 
                           db=db, 
                           charset=charset, 
                           use_unicode=use_unicode)
    
    def getConnection(self):
        return self.conn
    
    def close(self):
        self.conn.close()
        
    
if __name__ == '__main__':
    pass
#     
#     conn_factory = ConnectionFactory(host, user, passwd, db, charset, use_unicode)
#     print conn_factory.getConnection()
#     conn_factory.close()
    
    
