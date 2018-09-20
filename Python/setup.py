#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:28:58 2018

@author: petermoore
"""

# set up project working directory
PATH_HOME="/Users/petermoore/Documents/GitHub/VacationVision/Python"
PATH_CONNYAML = "connections.yaml" #NB this file ignored from GitHub
PATH_AUTHYAML = "authorisations.yaml" #NB this file ignored from GitHub
import os
os.chdir(PATH_HOME)




####### DATABASE #######

# create a function to read yaml file and get connection strings (0=SQL, 1=MONGO)
def getDSNfromYAML(yamlfile, yamlindex):
    import yaml
    with open(yamlfile, 'r') as f:
        doc = yaml.load(f)
        pdsn = doc[yamlindex]["DSN"]
        puser = doc[yamlindex]["user"]
        ppassword = doc[yamlindex]["password"]
        pport = doc[yamlindex]["port"]
        pdb = doc[yamlindex]["database"]
    dsn="DSN="+pdsn+";UID="+puser+";PWD="+ppassword
    alchemydsn = "mssql+pyodbc://"+puser+":"+ppassword+"@"+pdsn
    mongopath="mongodb://%s:%s@127.0.0.1:5174" % (puser, ppassword)
    return dsn, alchemydsn, pdsn, puser, ppassword, pport, pdb, mongopath


####### SQL #######
pyodbcdsn, sqlalchemydsn, rawdsn, sqluser, sqlpassword, sqlport, sqldb, _ = getDSNfromYAML(PATH_CONNYAML, 0)

# use sqlalchemy to talk to sql server via the Base, engine and session objects created here 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine(sqlalchemydsn)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine.execution_options(isolation_level='READ COMMITTED'))
session = DBSession()
####### END SQL #######

####### Mongo #######
_, _, _, mongouser, mongopassword, mongoport, mongodb, mongopath = getDSNfromYAML(PATH_CONNYAML, 1)
# code partially inspired by https://marcobonzanini.com/2015/09/07/getting-started-with-mongodb-and-python/
from pymongo import MongoClient
client = MongoClient(mongopath)
mongoengine = client[mongodb]
####### END MONGO #######

####### END DATABASE #######

####### SOCIAL MEDIA #######
# create a function to read yaml file and get authorisation strings (0=Twitter, 1=MONGO)
def getDSNfromYAML(yamlfile, 
                   yamlindex):
    import yaml
    with open(yamlfile, 'r') as f:
        doc = yaml.load(f)
        pplatform = doc[yamlindex]["platform"]
        pconsumerkey = doc[yamlindex]["consumerkey"]
        pconsumersecret = doc[yamlindex]["consumersecret"]
        paccesstoken = doc[yamlindex]["accesstoken"]
        paccesssecret = doc[yamlindex]["accesssecret"]
    return pplatform, pconsumerkey, pconsumersecret, paccesstoken, paccesssecret

####### TWITTER #######
# get twitter strings to set up connection
_, twitterconsumerkey, twitterconsumersecret, twitteraccesstoken, twitteraccesssecret = getDSNfromYAML(PATH_AUTHYAML, 0)
import tweepy
from tweepy import OAuthHandler
twitterauth = OAuthHandler(twitterconsumerkey, twitterconsumersecret)
twitterauth.set_access_token(twitteraccesstoken, twitteraccesssecret)
twitterapi = tweepy.API(twitterauth)

# get a user's timeline from https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
def gettimeline(api,
                username,
                include_rts=False,
                exclude_replies=True
                ):
    tweets = api.user_timeline(screen_name=username,
                               count=200, include_rts=include_rts,
                               exclude_replies=exclude_replies)

    last_id = tweets[-1].id
    while (True):
        more_tweets = api.user_timeline(screen_name=username,
                                    count=200,
                                    include_rts=include_rts,
                                    exclude_replies=exclude_replies,
                                    max_id=last_id-1)
        # There are no more tweets
        if (len(more_tweets) == 0):
              break
        else:
              last_id = more_tweets[-1].id-1
              tweets = tweets + more_tweets

    return tweets

def process_or_store(tweet):
    import json
    print(json.dumps(tweet))
    
#i = 0
#tweets = gettimeline(twitterapi, "thedatabloke")
#for tweet in tweets:
#    process_or_store(tweet._json)
#    i += 1
#    if i>3:
#        break
    
####### END TWITTER #######

####### END SOCIAL MEDIA #######