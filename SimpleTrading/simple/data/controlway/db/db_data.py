'''
Created on 2016. 7. 15.

@author: lee
'''




class DbData():
    
    def __init__(self):
        pass
    def set_data(self, host, user, passwd, db, charset, use_unicode):
        db_data.host = host
        db_data.user = user
        db_data.passwd = passwd
        db_data.db = db
        db_data.charset = charset
        db_data.use_unicode = use_unicode
        
    def get_db_data(self):
        return db_data

db_data = DbData()