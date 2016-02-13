import sqlite3
import os.path
import time

class sqliteDB(object):
	'''
	Base class to access local sqlite database
	'''
	def __init__(self):
		self.filepath = ''
		self.sqlcount = 0
		self.conn = ''
	
	def connect(self,file):
		#// if file exists
		if os.path.isfile(file) == 1:
			self.filepath = file
			try:
				self.conn = sqlite3.connect(self.filepath)
				return True
			except:
				print('Unable to connect to database.')
				return False
		else:
			print('Database is not found')
			return False

	def dbSQL(self,sSQL,etime=''):
		'''
		Execute sql query and print elapsed time if needed
		'''
		
		#// check if valid sql
		if etime==1: 
			start_time = time.clock()
		if len(sSQL) > 0:
			try:
				c = self.conn.cursor()
				c.execute(sSQL)
				self.conn.commit()
				result = c.fetchall()
			except:
				result = None
		else:
			print("Empty SQL statement.")
		
		#// increment counter
		self.sqlcount += 1

		if etime==1:
			print('--- Executed in %s seconds ---' % str(time.clock() - start_time))
		if result:
			return result
		else:
			return False
			
	def getLastInsert(self):
		c = self.conn.cursor()
		sSQL = "SELECT last_insert_rowid();"
		c.execute(sSQL)
		result=c.fetchone()
		return result[0]

	def dbClose(self):
		self.dbOptimizeReset()
		self.conn.close()	

	def dbStartTransaction(self):
		sSQL = 'BEGIN TRANSACTION;'
		self.dbSQL(sSQL)
		
	def dbEndTransaction(self):
		sSQL = 'END TRANSACTION;'
		result=self.dbSQL(sSQL)
		
	def dbOptimize(self):
		sSQL = 'PRAGMA synchronous = OFF'
		self.dbSQL(sSQL)

		sSQL = 'PRAGMA journal_mode = MEMORY'
		self.dbSQL(sSQL)
		
	def dbOptimizeReset(self):
		sSQL = 'PRAGMA synchronous = ON'
		result=self.dbSQL(sSQL)

		sSQL = 'PRAGMA journal_mode = DELETE'
		result=self.dbSQL(sSQL)	
		
	def dbSchema(self,table=''):
		if table:
			sSQL = 'SELECT * FROM sqlite_master WHERE name = "' + table + '";'
		else:
			sSQL = 'SELECT * FROM sqlite_master;'
		result=self.dbSQL(sSQL)
	
		return result

	def dbTables(self,table=''):
		if table:
			sSQL = 'SELECT name FROM sqlite_master WHERE name = "' + table + '";'
		else:
			sSQL = 'SELECT name FROM sqlite_master;'
		result=self.dbSQL(sSQL)
		return result
	
	def dbSQLCount(self):
		return self.sqlcount
	

