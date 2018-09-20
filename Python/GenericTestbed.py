#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:16:12 2018

@author: petermoore
"""
#from objectclasses import Version
from setup import pyodbcdsn,session

#region sqltestbed
from SQLFunctionality import sqldf
_dataframe = sqldf("SELECT db_name()", pyodbcdsn)

from ObjectClasses import Version
ns=Version()
ns.Version='Version 3'
_Version = ns.addappend(session)
#endregion sqltestbed

#region mongotestbed
from setup import mongoengine
from MongoFunctionality import mongoAppend
somedict = {
   "title": "An article about MongoDB and Python",
   "author": "Frederick"
   # more fields
}
mongoAppend(doc=somedict, mongoengine = mongoengine, mongocoll="NameOfCollection")
#endregion mongotestbed

#region twittertestbed
from TwitterFunctionality import twitterGetTimeline, twitterPrintTweetJSON
from setup import twitterapi
i = 0
tweets = twitterGetTimeline(twitterapi, "thedatabloke")
for tweet in tweets:
   twitterPrintTweetJSON(tweet)
   i += 1
   if i>3:
       break
#endregion twittertestbed