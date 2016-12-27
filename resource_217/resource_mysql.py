import pymysql
import os.path
import time

class mysqlDB(object):
	'''
	Base class to access local sqlite database
	'''
	def __init__(self):
		self.filepath = ''
		self.sqlcount = 0
		self.conn = ''

	def connect(self, host='localhost', port=3306, user='', passwd='', db=''):
	'''
	Open a connection to a database.
	'''
		try:
			self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
			return True
		except:
			print('Unable to connect to database.')
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
				print('SQL Failed')
		else:
			print("Empty SQL statement.")

		#// increment counter
		self.sqlcount += 1

		if etime==1:
			print('--- Executed in %s seconds ---' % str(time.clock() - start_time))
		if result is not None:
			return result
		else:
			return None

	def getLastInsert(self):
		'''
		Get result of last query.
		'''
		c = self.conn.cursor()
		#sSQL = "SELECT last_insert_rowid();"
		sSQL = 'SELECT LAST_INSERT_ID();'
		c.execute(sSQL)
		result=c.fetchone()
		return result[0]

	def dbClose(self):
		'''
		Close the active database.
		'''
		self.conn.close()

	def dbStartTransaction(self):
		'''
		Start a SQL transaction.
		'''
		sSQL = 'START TRANSACTION;'
		self.dbSQL(sSQL)

	def dbEndTransaction(self):
		'''
		End a SQL transaction.
		'''
		sSQL = 'COMMIT;'
		result=self.dbSQL(sSQL)

	def dbSchema(self,table=''):
		'''
		Show a description for a table.
		'''
		if table:
			sSQL = 'describe ' + table + ';'
		else:
			sSQL = 'show tables;'
		result=self.dbSQL(sSQL)

		return result

	def dbTables(self,table=''):
		'''
		Show a list of tables in the active database.
		'''
		if table:
			sSQL = 'show tables;'
		else:
			sSQL = 'show tables;'
		result=self.dbSQL(sSQL)
		return result

	def dbSQLCount(self):
		'''
		Display SQL queries in session.
		'''
		return self.sqlcount
