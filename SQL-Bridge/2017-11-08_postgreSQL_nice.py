#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-11-08_postgreSQL_nice.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 08/11/2017
#------------------------------------------------------------
''' Intro to using encapsulated access to PostgreSQL databases
	-converted to python 3
	-disabled schemas
	-ini file contains database params
	-BookGetter class should host the database commands
	http://www.andreafiori.net/posts/connecting-to-a-postgresql-database-with-python
	Further reading:
	Common problems here:
	http://initd.org/psycopg/docs/faq.html#faq-compile
	Dynamic statements:
	http://initd.org/psycopg/docs/sql.html#module-psycopg2.sql
'''
from lib.database import Database

class BookGetter:
	def __init__(self, database):
		self.db = database
	def getBooks(self):
		query = "SELECT id, title, author FROM books"
		return self.db.fetchAll(query)
	def getBook(self, id):
		query = "SELECT id, title, author FROM books WHERE id = {}; ". format(id)
		return self.db.fetchOne(query)

db = Database()

bookGetter = BookGetter(db)
bookList = bookGetter.getBooks()
for book in bookList:
	print(book['id'], '', book['title'])

db.closeDb()

