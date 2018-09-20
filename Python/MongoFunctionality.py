#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:11:35 2018
A collection of functions for querying the mongo database
@author: petermoore
"""





# code to append a json file "doc" to the mongo db as defined by mongoengine, to the collection as defined by mongocoll
def mongoAppend(doc, mongoengine, mongocoll):
    # example usage:
    # from setup import mongoengine
    # mongoAppend(doc=somedict, mongoengine = mongoengine, mongocoll="NameOfCollection")
    coll = mongoengine[mongocoll]
    return coll.insert_one(doc).inserted_id # NB The _id of a document is an instance of ObjectId, rather than a simple string



