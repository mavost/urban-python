#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-11-07_postgreSQL.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 07/11/2017
#------------------------------------------------------------
''' 
Query a database with login details specified in ini file
Common problems here:
http://initd.org/psycopg/docs/faq.html#faq-compile
Dynamic statements:
http://initd.org/psycopg/docs/sql.html#module-psycopg2.sql

http://initd.org/psycopg/docs/connection.html

connect to PostgreSQL DB installed on machine
port:	5432
user:	postgres
pwd:	root
postgresql://user:root@localhost/mydb:5432
'''
import pprint
import psycopg2 as pg

'''
DSN="dbname='uebungsdatenbank' user='postgres' password='root' port='5432' host='localhost'"
print(DSN)
conn = pg.connect(DSN)

# IMPORTANT http://initd.org/psycopg/docs/usage.html
with conn:							
	with conn.cursor() as curs:		
		curs.execute("SELECT name, vorname FROM mitarbeiter WHERE name LIKE 'L%';")
		data=curs.fetchall()		
	#closing cursor
#closing transaction but not connection

conn.close()
pprint.pprint(str(data))
print(str(data))
'''

# create database on server
DSN="dbname='postgres' user='postgres' password='root' port='5432' host='localhost'"
print(DSN)
conn = pg.connect(DSN)
with conn:
	conn.autocommit=True
	with conn.cursor() as curs:		
		curs.execute("CREATE DATABASE suppliers ENCODING 'UTF8'")
conn.close()

# create tables in database
# http://www.postgresqltutorial.com/postgresql-python/create-tables/
commands = (
		"""
		CREATE TABLE vendors (
			vendor_id SERIAL PRIMARY KEY,
			vendor_name VARCHAR(255) NOT NULL
		)
		""",
		""" CREATE TABLE parts (
				part_id SERIAL PRIMARY KEY,
				part_name VARCHAR(255) NOT NULL
				)
		""",
		"""
		CREATE TABLE part_drawings (
				part_id INTEGER PRIMARY KEY,
				file_extension VARCHAR(5) NOT NULL,
				drawing_data BYTEA NOT NULL,
				FOREIGN KEY (part_id)
				REFERENCES parts (part_id)
				ON UPDATE CASCADE ON DELETE CASCADE
		)
		""",
		"""
		CREATE TABLE vendor_parts (
				vendor_id INTEGER NOT NULL,
				part_id INTEGER NOT NULL,
				PRIMARY KEY (vendor_id , part_id),
				FOREIGN KEY (vendor_id)
					REFERENCES vendors (vendor_id)
					ON UPDATE CASCADE ON DELETE CASCADE,
				FOREIGN KEY (part_id)
					REFERENCES parts (part_id)
					ON UPDATE CASCADE ON DELETE CASCADE
		)
		""")

DSN="dbname='suppliers' user='postgres' password='root' port='5432' host='localhost'"
print(DSN)
conn = None
try:
	# connect to the PostgreSQL server
	conn = pg.connect(DSN)
	curs = conn.cursor()
	print('PostgreSQL database version:')
	curs.execute('SELECT version()')
	# display the PostgreSQL database server version
	db_version = curs.fetchone()
	print(db_version)
	# create table one by one
	for command in commands:
		curs.execute(command)
	# close communication with the PostgreSQL database server
	curs.close()
	# commit the changes
	conn.commit()
except (Exception, pg.DatabaseError) as error:
	print(error)
finally:
	if conn is not None:
		conn.close()
