#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: chap32_gender.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 25/10/2017
#------------------------------------------------------------
''' Python 3 main - "Big Data" mining example
'''
from multiprocessing import Pool
from time import time

WORD, GENDER = "car", "male"
ANSWER = """Number of Tweets in %s category : %i of %i
The word %s has been found in %8.3f Percent of all tweets
Processing time %5.2f""" 

def search(line):
	gender_found, word_found=0,0;
	if GENDER in line:
		gender_found+=1
		if WORD in line:
			word_found+=1
	return gender_found, word_found

if __name__ == "__main__":				# 1) protects us from infinite recursion calls caused by sub-process p1
	f=open("data/gender-classifier-DFE-791531.csv", 'r', encoding="ansi") #utf-8 encoding threw a bug in windows
	data=f.readlines()
	f.close()
	start=time()
	p1 = Pool()
#	results=p1.map(search,data) #0.81s
	results=p1.map(search,data,chunksize=2000) #0.75s processing with two cores
	gs_f, ws_f = zip(*results)
	p1.close()
	p1.join()
	g_c=sum(gs_f)
	w_c=sum(ws_f)
	print(ANSWER % (GENDER, g_c, len(data), WORD, w_c/g_c, time()-start))
