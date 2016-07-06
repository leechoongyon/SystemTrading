# -*- coding: utf-8 -*-
import MySQLdb as mdb

class DataHandler():
	def __init__(self, host, user, passwd, db, charset, use_unicode):
		self.conn = mdb.connect(host=host, 
                             	user=user, 
                              	passwd=passwd, 
							  	db=db, 
                             	charset=charset, 
                              	use_unicode=use_unicode);

	def beginTrans(self):
		self.conn.autocommit(False)

	def endTrans(self):
		try:
			self.conn.commit()
			self.conn.autocommit(True)
		except Exception, e:
			print "Fatal Error in commit !!!"
			print e
			self.conn.rollback()


	def openSql(self,sql):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			return cursor
		except Exception as e:
			print ">>> Unexpected error in openSQL: ", e
			print "--- %s ---" % (sql)
			raise
	
	def execSql(self,sql,db_commit=True):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			if db_commit:
				self.conn.commit()
			return cursor
		except Exception as e:
			print ">>> Unexpected error in ExecSQL: ", e
			print "--- %s ---" % (sql)
	
	def execSqlWithParam(self, sql, param, db_commit=True):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql, param)
			if db_commit:
				self.conn.commit()
			return cursor
		except Exception as e:
			print ">>> Unexpected error in ExecSQL: ", e
			print "--- %s ---" % (sql)
		
	
	def execSqlMany(self, sql, param, db_commit=True):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			if db_commit:
				self.conn.commit()
			return cursor
		except Exception as e:
			print ">>> Unexpected error in ExecSQL: ", e
			print "--- %s ---" % (sql)
			self.conn.rollback()
			
	def execSqlManyWithParam(self, sql, param, db_commit=True):
		try:
			cursor = self.conn.cursor()
			cursor.executemany(sql, param)
			if db_commit:
				self.conn.commit()
			return cursor
		except Exception as e:
			print ">>> Unexpected error in ExecSQL: ", e
			print "--- %s ---" % (sql)
			self.conn.rollback()

if __name__ == '__main__':
	pass
	
