#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:16:12 2018

@author: petermoore
"""
from objectclasses import Section
from setup import session, sqldf, pyodbcdsn, mongoengine


_dataframe = sqldf("SELECT db_name()", pyodbcdsn)

ns=Section()
ns.section='Section'
_section = ns.addappend(session)

coll = mongoengine['articles']

doc = {
    "title": "An article about MongoDB and Python",
    "author": "Susan"
    # more fields
}


doc_id = coll.insert_one(doc).inserted_id # NB The _id of a document is an instance of ObjectId, rather than a simple string


# query by ObjectId
my_doc = coll.find_one({'_id' : doc_id})
print(my_doc)