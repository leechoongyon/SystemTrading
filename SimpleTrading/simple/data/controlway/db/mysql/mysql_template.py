'''
Created on 2016. 6. 30.

@author: lee
'''



class MySqlTemplate:
    
    def __init__(self, conn):
        self.conn = conn
    
    def selectList(self, sql):
        try :
            cursor = self.conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception, e:
            print e
        finally:
            cursor.close() 
        
    def selectWithParam(self,sql, param):
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, param)
            results = cursor.fetchall()
            return results
        except Exception, e:
            print e
        finally:
            cursor.close()
    
    
    def insertOne(self):
        pass

    def insertMany(self, sql, param):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(sql, param)
            self.commit()
            
        except Exception, e:
            print e
            self.conn.rollback()
            
        finally:
            cursor.close()
    
    def updateWithParam(self, sql, param):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, param)
            self.commit()
        except Exception, e:
            print e
            self.conn.rollback()
            
        finally:
            cursor.close()
    
    def updateManyWithParam(self, sql, param):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(sql, param)
            self.commit()
        except Exception, e:
            print e
            self.conn.rollback()
            
        finally:
            cursor.close()
            
    
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()