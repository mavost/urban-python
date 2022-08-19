#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: video06_sql_test.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 26/10/2017
#------------------------------------------------------------
''' Python 3 main - creating an SQL database
'''

import sqlite3 

connection=sqlite3.connect('data/bmi.db')
cursor=connection.cursor()
cursor.execute('''DROP TABLE IF EXISTS bmirechner''')
cursor.execute('''CREATE TABLE bmirechner(id INTEGER PRIMARY KEY, name TEXT, bmi REAL)''')
cursor.execute('''INSERT INTO bmirechner VALUES(?,?,?)''', (1,'Markus', 22.1)) # using secure transmission?
cursor.execute('''INSERT INTO bmirechner VALUES(?,?,?)''', (2,'Peter', 18.1))
cursor.execute('''INSERT INTO bmirechner VALUES(?,?,?)''', (3,'Sven', 17.1222))

cursor.execute('''SELECT bmi,name FROM bmirechner WHERE bmi<=20''')
rows=cursor.fetchall()
print(rows)
connection.close()

