#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:02:17 2018

@author: petermoore
"""

# code partially inspired by https://marcobonzanini.com/2015/09/07/getting-started-with-mongodb-and-python/
from pymongo import MongoClient
username = "mongosa"
password = "D1st1nct10n"
 
client = MongoClient('mongodb://%s:%s@127.0.0.1:5174' % (username, password))

db = client['tutorial']
coll = db['articles']



from datetime import datetime
 
doc = {
    "title": "An article about MongoDB and Python",
    "author": "Marco",
    "publication_date": datetime.utcnow(),
    # more fields
}
 
doc_id = coll.insert_one(doc).inserted_id # NB The _id of a document is an instance of ObjectId, rather than a simple string


# query by ObjectId
my_doc = coll.find_one({'_id' : doc_id})
print(my_doc)



