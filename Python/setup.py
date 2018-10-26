#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:28:58 2018

@author: petermoore
"""

# set up project working directory
PATH_HOME = "/Users/petermoore/Documents/GitHub/VacationVision/Python"
PATH_CONNYAML = "connections.yaml"  # NB this file ignored from GitHub
PATH_AUTHYAML = "authorisations.yaml"  # NB this file ignored from GitHub
import os
os.chdir(PATH_HOME)

# region DATABASE
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
    dsn = "DSN="+pdsn+";UID="+puser+";PWD="+ppassword
    alchemydsn = "mssql+pyodbc://"+puser+":"+ppassword+"@"+pdsn
    mongopath = "mongodb://%s:%s@127.0.0.1:6173" % (puser, ppassword)
    return dsn, alchemydsn, pdsn, puser, ppassword, pport, pdb, mongopath


# region SQL

# connection strings
pyodbcdsn, sqlalchemydsn, rawdsn, sqluser, sqlpassword, sqlport, sqldb, _ = getDSNfromYAML(
    PATH_CONNYAML, "sqlconn")

# sqlalchemy engine: use sqlalchemy to talk to sql server via the Base, engine and session objects created here
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(sqlalchemydsn)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine.execution_options(
    isolation_level='READ COMMITTED'))
session = DBSession()
# endregion SQL

# region MONGO
_, _, _, mongouser, mongopassword, mongoport, mongodb, mongopath = getDSNfromYAML(
    PATH_CONNYAML, "mongoconn")
# mongo engine: code partially inspired by https://marcobonzanini.com/2015/09/07/getting-started-with-mongodb-and-python/
from pymongo import MongoClient
client = MongoClient(mongopath)
mongoengine = client[mongodb]
listing = mongoengine.command('usersInfo')
for document in listing['users']:
    print(document['user'] +" "+ document['roles'][0]['role'])
# endregion MONGO

# endregion DATABASE

# region SOCIALMEDIA
# create a function to read yaml file and get authorisation strings (0=Twitter, 1=MONGO)


def getAuthDSNfromYAML(yamlfile,
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


# region TWITTER
# get twitter strings to set up connection
_, twitterconsumerkey, twitterconsumersecret, twitteraccesstoken, twitteraccesssecret = getAuthDSNfromYAML(
    PATH_AUTHYAML, 0)
import tweepy
from tweepy import OAuthHandler
twitterauth = OAuthHandler(twitterconsumerkey, twitterconsumersecret)
twitterauth.set_access_token(twitteraccesstoken, twitteraccesssecret)
twitterapi = tweepy.API(twitterauth)

# endregion TWITTER

# endregion SOCIALMEDIA
