#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: database.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 08/11/2017
#------------------------------------------------------------
''' Intro to using encapsulated access to PostgreSQL databases
	-converted to python 3
	-disabled schemas
	-ini file contains database params
	http://www.andreafiori.net/posts/connecting-to-a-postgresql-database-with-python
	Further reading:
	Common problems here:
	http://initd.org/psycopg/docs/faq.html#faq-compile
	Dynamic statements:
	http://initd.org/psycopg/docs/sql.html#module-psycopg2.sql
'''

import psycopg2
import psycopg2.extras
from lib.configurations import Configurations

class Database:
	def __init__(self):
		configurations = Configurations()
		self.configParser = configurations.getConfigParser()
		self.conn = psycopg2.connect("host='{}' dbname='{}' user='{}' password='{}'". format( self.configParser.get('POSTGRESQL', 'host'), self.configParser.get('POSTGRESQL', 'dbname'), self.configParser.get('POSTGRESQL', 'username'), self.configParser.get('POSTGRESQL', 'password') ))
		print("Opening database")
		cur = self.conn.cursor()
		#schema = self.configParser.get('POSTGRESQL', 'schema')
		#if schema is not None and schema != '':
		#	cur.execute("SET search_path TO {}". format(schema) )

	def getDbConnection(self):
		return self.conn

	def fetchAll(self, query):
		cur = self._executeQuery(query)
		rows = cur.fetchall()
		return rows

	def fetchOne(self, query):
		cur = self._executeQuery(query)
		rows = cur.fetchone()
		return rows

# Execute the query and return the cursor object
	def _executeQuery(self, query):
		cur = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
		cur.execute(query)
		return cur

	def closeDb(self):
		print("Closing database")
		self.conn.close()
