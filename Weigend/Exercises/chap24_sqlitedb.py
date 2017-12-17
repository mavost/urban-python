#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap24_sqlitedb.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 11/12/2017
#------------------------------------------------------------
''' Python 3 main - Using the sqlitedb to create a small relational database

	


'''

import sqlite3

PATH='./data/example.db'

PERSONS = {'Tom': '072102010',
			'Anna': '07210210999',
			'Mike': '0643229'}

SQL_CREATE = """CREATE TABLE contact(name VARCHAR(100), phone VARCHAR(20), test BINARY(16))"""
			
SQL_INSERT_1 = """INSERT INTO contact VALUES ('{}', '{}')"""
SQL_INSERT_2 = """INSERT INTO contact VALUES (?, ?, ?)"""

SQL_SELECT = """SELECT * FROM contact WHERE phone LIKE '07%'"""

connection = sqlite3.connect(PATH)

cursor = connection.cursor()
print('connection opened')

cursor.execute(SQL_CREATE)

for person in PERSONS:
	#print(SQL_INSERT.format(person, PERSONS[person]))
	#cursor.execute(SQL_INSERT_1.format(person, PERSONS[person]))		#bad idea for security reasons - SQL injection
	cursor.execute(SQL_INSERT_2, (person, PERSONS[person], b"avbsdwe"))
print('write successful')

result = cursor.execute(SQL_SELECT)			#returns iterator of resulting rows
for row in result:
	print(row)								#row contains tuple
	
print('output successful')


connection.commit()
cursor.close()
connection.close()
print('connection closed')
