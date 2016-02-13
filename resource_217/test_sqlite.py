#// temp inport for testing
import sys
import random
import time

from resource_sqlite import sqliteDB

def main():
	r = 2500
	
	test_start_time = time.time()
	 
	#// define database filename	
	dbfilename='database.db'
			
	db = sqliteDB()
	if not db.connect(dbfilename):
		sys.exit()
		
	print('\nTest#1 - Dispay schema for all tables')
	result = db.dbSchema()
	for line in result:
		print(line)
		
	print('\nTest#2 - Dispay schema for table')
	result = db.dbSchema(table='nodes')

	for line in result:
		print(line)
		
	print('\nTest#3 - Dispay table names')
	result = db.dbTables()
	for line in result:
		print(line)
		
	print('\nTest#4 - Dispay one table name')
	result = db.dbTables(table='devices')

	for line in result:
		print(line)
	
	print('\nTest#5 - insert a record')
	r_key = 'key' + str(random.randrange(1000))
	r_value = str(random.randrange(9999))
	sSQL = 'INSERT INTO devices (skey,svalue) VALUES ("' + r_key + '","' + r_value + '");'
	result = db.dbSQL(sSQL)
	
	print('\nTest#6 - get id from last insert')
	result = db.getLastInsert()
	print('Last insert id: ' + str(result))
	
	
	print('\nTest#7 - insert ' + str(r) + ' records')
	start_time = time.time()
	print('Inserting ' + str(r) + ' random records.' )
	for i in range(r):
		r_key = 'key' + str(random.randrange(1000))
		r_value = str(random.randrange(9999))
		sSQL = 'INSERT INTO devices (skey,svalue) VALUES ("' + r_key + '","' + r_value + '");'
		result = db.dbSQL(sSQL)
	print('--- Executed in %s seconds ---' % str(time.time() - start_time))

	print('\nTest#8 - insert ' + str(r) + ' records with transaction')
	print('Note: Start Transaction')
	start_time = time.time()
	db.dbStartTransaction()
	#r = random.randrange(1800,2000)
	print('Inserting ' + str(r) + ' random records.' )
	for i in range(r):
		r_key = 'key' + str(random.randrange(1000))
		r_value = str(random.randrange(9999))
		sSQL = 'INSERT INTO devices (skey,svalue) VALUES ("' + r_key + '","' + r_value + '");'
		result = db.dbSQL(sSQL)
	
	print('Note: Commit Transaction')
	db.dbEndTransaction()
	print('--- Executed in %s seconds ---' % str(time.time() - start_time))
	
	print('\nTest#9 - insert ' + str(r) + ' records with optimize')
	print('Note: DB optimize on.')
	db.dbOptimize()
	r = random.randrange(1800,2000)
	print('Inserting ' + str(r) + ' random records.' )
	for i in range(r):
		r_key = 'key' + str(random.randrange(1000))
		r_value = str(random.randrange(9999))
		sSQL = 'INSERT INTO devices (skey,svalue) VALUES ("' + r_key + '","' + r_value + '");'
		result = db.dbSQL(sSQL)
	
	print('Note: DB optimize reset.')
	db.dbOptimizeReset()
	print('--- Executed in %s seconds ---' % str(time.time() - start_time))
	
	print('\nTest#10 - display values')
	sSQL = 'SELECT * FROM devices WHERE id < 5;'
	result = db.dbSQL(sSQL)
	print(result)

	print('\nTest#11 - retrieve result and then count values')
	sSQL = 'SELECT * FROM devices WHERE id < 5;'
	result = db.dbSQL(sSQL)
	print(len(result))

	print('\nTest#12 - display values one at a time')
	for line in result:
		print(line)

		
	print('\nTest#11 - display SQL queries in session')	
	print('SQL queries: ', db.dbSQLCount())


	print('\nTest#13 - display record count for table')
	sSQL = 'SELECT COUNT(id) FROM devices;'
	result = db.dbSQL(sSQL)
	print(result)

	#// close database 
	db.dbClose()
	print('--- Executed in %s seconds ---' % str(time.time() - test_start_time))

def main_database_test():
	sSQL = 'INSERT INTO devices (skey,svalue) VALUES ("' + r_key + '","' + r_value + '");'
	sSQL = 'SELECT * FROM devices;'
	conn = sqlite3.connect(dbfilename)
	conn.execute(sSQL)
	conn.commit()

	c = conn.cursor()
	c.execute(sSQL)
	result=c.fetchall()
	print(result)
	
	
if __name__ == '__main__':
	main()
