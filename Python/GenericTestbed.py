#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:16:12 2018

@author: petermoore
"""
#from objectclasses import Version
from setup import pyodbcdsn,session

from SQLFunctionality import sqldf

_dataframe = sqldf("SELECT db_name()", pyodbcdsn)

from ObjectClasses import Version
ns=Version()
ns.Version='Version 3'
_Version = ns.addappend(session)


#
#coll = mongoengine['articles2']
#
#doc = {
#    "title": "An article about MongoDB and Python",
#    "author": "Stephen"
#    # more fields
#}
#
#
#doc_id = coll.insert_one(doc).inserted_id # NB The _id of a document is an instance of ObjectId, rather than a simple string
#
#
## query by ObjectId
#my_doc = coll.find_one({'_id' : doc_id})
#print(my_doc)