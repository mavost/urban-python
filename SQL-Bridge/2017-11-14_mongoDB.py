#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2017-11-14_mongoDB.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 14/11/2017
#------------------------------------------------------------
''' Intro to using MongoDB databases with the pymongo driver
	https://api.mongodb.com/python/current/tutorial.html
'''
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')		#connect using the MongoDB URI format

client.database_names()									#list databases on current mongo server

db = client.test										#connect to database
#db = client['test']									#alternatively connect using dict style

db.collection_names()									#list collections withing database
res=db.array.find_one()									#return first object
print(res)


'''
https://stackoverflow.com/questions/23909975/do-i-need-to-close-connection-in-mongodb

# Create your views here.
from pymongo import MongoClient
import pymongo
from pymongo import Connection
import json
from bson import BSON
from bson import json_util


class MongoConnection():
    def __init__ (self, host="localhost",port=27017, db_name='indexer', conn_type="local", username='', password=''):
        self.host = host
        self.port = port
        self.conn = Connection(self.host, self.port)
        self.db = self.conn[db_name]
        self.db.authenticate(username, password)

    def ensure_index(self, table_name, index=None):
        self.db[table_name].ensure_index([(index,pymongo.GEOSPHERE)])

    def create_table(self, table_name, index=None):
        self.db[table_name].create_index( [(index, pymongo.DESCENDING)] )


    def get_one(self,table_name,conditions={}):
        single_doc = self.db[table_name].find_one(conditions)
        json_doc = json.dumps(single_doc,default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(json_doc)

    def get_all(self,table_name,conditions={}, sort_index ='_id', limit=100):
        all_doc = self.db[table_name].find(conditions).sort(sort_index, pymongo.DESCENDING).limit(limit)
        json_doc = json.dumps(list(all_doc),default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(str(json_doc))


    def insert_one(self, table_name, value):
        self.db[table_name].insert(value)

    def update_push(self, table_name, where, what):
        #print where, what
        self.db[table_name].update(where,{"$push":what},upsert=False)

    def update(self, table_name, where, what):
        #print where, what
        self.db[table_name].update(where,{"$set":what},upsert=False)

    def update_multi(self, table_name, where, what):
        self.db[table_name].update(where,{"$set":what},upsert=False, multi=True)

    def update_upsert(self, table_name, where, what):
        self.db[table_name].update(where,{"$set":what},upsert=True)


    def map_reduce(self, table_name, mapper, reducer, query, result_table_name):
        myresult = self.db[table_name].map_reduce(mapper, reducer, result_table_name, query)
        return myresult

    def map_reduce_search(self, table_name, mapper, reducer,query, sort_by, sort = -1, limit = 20):
        if sort_by == "distance":
            sort_direction = pymongo.ASCENDING
        else:
            sort_direction = pymongo.DESCENDING
        myresult = self.db[table_name].map_reduce(mapper,reducer,'results', query)
        results = self.db['results'].find().sort("value."+sort_by, sort_direction).limit(limit)
        json_doc = json.dumps(list(results),default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(str(json_doc))

    def aggregrate_all(self,table_name,conditions={}):
        all_doc = self.db[table_name].aggregate(conditions)['result']
        json_doc = json.dumps(list(all_doc),default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(str(json_doc))

    def group(self,table_name,key, condition, initial, reducer):
        all_doc = self.db[table_name].group(key=key, condition=condition, initial=initial, reduce=reducer)
        json_doc = json.dumps(list(all_doc),default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(str(json_doc))

    def get_distinct(self,table_name, distinct_val, query):
        all_doc = self.db[table_name].find(query).distinct(distinct_val)
        count = len(all_doc)        
        parameter = {}
        parameter['count'] = count
        parameter['results'] = all_doc
        return parameter

    def get_all_vals(self,table_name,conditions={}, sort_index ='_id'):
        all_doc = self.db[table_name].find(conditions).sort(sort_index, pymongo.DESCENDING)
        json_doc = json.dumps(list(all_doc),default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(json_doc)

    def get_paginated_values(self, table_name, conditions ={}, sort_index ='_id', pageNumber = 1):
        all_doc = self.db[table_name].find(conditions).sort(sort_index, pymongo.DESCENDING).skip((pageNumber-1)*15).limit(15)
        json_doc = json.dumps(list(all_doc),default=json_util.default)
        json_doc = json_doc.replace("$oid", "id")
        json_doc = json_doc.replace("_id", "uid")
        return json.loads(json_doc)        

    def get_count(self, table_name,conditions={}, sort_index='_id'):
        count = self.db[table_name].find(conditions).count()
        return count
'''