#!/Python36-32/python.exe #Windows shebang 
#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap25_unittest.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 13/12/2017
#------------------------------------------------------------
''' Python 3 main - An example for testing using the unittest module


'''
import unittest

import pickle 
class Ranking:										#1
	def __init__ (self, filename):
		self.filename = filename
		try:											#2
			f = open(filename, "rb")
			self.voting = pickle.load(f)
			f.close()
		except: self.voting = {}

	def add (self, word):							   #3
		if word in self.voting.keys():
			self.voting[word] += 1
		else: self.voting[word] = 1

	def getTop(self, n):
		items = [(self.voting[word], word)			  #4
			for word in self.voting.keys()]
		items.sort(reverse = True)					  #5
		top = items[:n]								 #6
		response = ""								   #7
		for (votes, word) in top:
			response += "{} {} <br> ".format(word, votes)
		return response

	def getRank (self, word):						   #8
		votes = self.voting[word]					   
		vote_list = list(self.voting.values())		  #9
		vote_list.sort(reverse = True)
		return vote_list.index(votes)+1				#10

	def save (self):
		f = open (self.filename, "wb")
		pickle.dump(self.voting, f)
		f.close()

class TestRanking(unittest.TestCase):
	def setUp(self):
		"""Generate list of words and Ranking instance"""
		self.words = ['Mars','Mars','Venus']
		self.r = Ranking('data/not_existing.txt')				#create an Instance without any data - see, __init__ exception

	def testF_add(self):									#define one scenario
		for word in self.words:							
			self.r.add(word)							#call the class function to be tested
		for word in self.r.voting.keys():
			n_voting = self.r.voting[word]				#result of class action 
			n_words = self.words.count(word)			#number of word in input list
			self.failUnless(n_voting == n_words)		#the actual test condition 
														#Other TestCase methods:
														#	assert_(<Expression>,[message]))						--- Equivalent to failUnless()
														#	assertEqual(<Var1>,<Var2>,[message]))					--- Equivalent to failUnlessEqual()
														#	assertAlmostEqual(<Var1>,<Var2>,[precision,[message]]) 	--- Comparing floats
														#	...

suite = unittest.TestSuite()							#compiling a set of test cases
test = TestRanking("testF_add")							#testing case containing one particular scenario
suite.addTest(test)										#submitting to TestSuite

testrunner = unittest.TextTestRunner(verbosity=2)				#create a testing bot which produces interpretable output
#testrunner = unittest.TextTestRunner(stream=sys.stdout)		#create a testing bot with error output to stdout instead of stderr
testrunner.run(suite)

