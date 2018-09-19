#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:28:58 2018

@author: petermoore
"""
PATH_HOME="/Users/petermoore/Documents/GitHub/VacationVision/Python"
import os
os.chdir(PATH_HOME)
print(os.getcwd())
PATH_CONNYAML = "connections.yaml" #NB this file ignored from GitHub

# function to read yaml file and get connection strings (0=SQL, 1=MONGO)
def getDSNfromYAML(yamlfile, yamlindex):
    import yaml
    with open(yamlfile, 'r') as f:
        doc = yaml.load(f)
        pdsn = doc[yamlindex]["DSN"]
        puser = doc[yamlindex]["user"]
        ppassword = doc[yamlindex]["password"]
        pport = doc[yamlindex]["port"]
    dsn="DSN="+pdsn+";UID="+puser+";PWD="+ppassword
    alchemydsn = "mssql+pyodbc://"+puser+":"+ppassword+"@"+pdsn
    return dsn, alchemydsn, pdsn, puser, ppassword, pport




pyodbcdsn, sqlalchemydsn, rawdsn, sqluser, sqlpassword, _ = getDSNfromYAML(PATH_CONNYAML, 0)
_, _, _, mongouser, mongopassword, mongoport = getDSNfromYAML(PATH_CONNYAML, 1)

def sqldf(sql,con):
    import pyodbc
    import pandas as pd
    conn = pyodbc.connect(con, autocommit=True)
    df = pd.read_sql(sql,conn)
    return df


#sqldf("SELECT db_name()", pyodbcdsn)
    

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine(sqlalchemydsn)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine.execution_options(isolation_level='READ COMMITTED'))
session = DBSession()

def sqlAppendIfNotExists(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        print("This record already exists in the " + instance.__tablename__ + " table")
    else:
        instance = model(**kwargs)
        session.add(instance)
    session.commit()
    return instance

from sqlalchemy import Column, Integer, String
class Section(Base):
    __tablename__='Section'
    sectionid= Column( Integer, primary_key=True, nullable=False )
    section= Column( String(50), nullable=False )
    def addappend(self, session):
        return sqlAppendIfNotExists(session, Section,
                                       section=self.section)


ns=Section()
ns.section='Section'
x = ns.addappend(session)
