#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:11:52 2018
A collection of functions for querying the sql database
@author: petermoore
"""

# make pandas data from from raw sql code via pyodbc 
def sqldf(sql,con):
    # example usage: 
#    from setup import pyodbcdsn
#    _dataframe = sqldf("SELECT db_name()", pyodbcdsn)
    import pyodbc
    import pandas as pd
    conn = pyodbc.connect(con, autocommit=True)
    df = pd.read_sql(sql,conn)
    return df


# create an insert if not exists function via sqlalchemy
# adapted from the get_or_create function here: https://stackoverflow.com/questions/2546207/does-sqlalchemy-have-an-equivalent-of-djangos-get-or-creat
def sqlAppendIfNotExists(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        print("This record already exists in the " + instance.__tablename__ + " table")
    else:
        instance = model(**kwargs)
        session.add(instance)
    session.commit()
    return instance