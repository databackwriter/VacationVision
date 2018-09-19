#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:06:20 2018

@author: petermoore

The classes herein will become tables in the database relating to engine as defined in setup.py
"""

# get sqlalchemy connection settings via setup.py
from setup import Base, engine
# get obectsqlalchemy object settings
from sqlalchemy import Column, Integer, String

# create an insert if not exists function
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

# sample class called section
class Section(Base):
    __tablename__='Section'
    sectionid= Column( Integer, primary_key=True, nullable=False )
    section= Column( String(50), nullable=False )
    def addappend(self, session):
        return sqlAppendIfNotExists(session, Section,
                                       section=self.section)
        
  # where the engine runs and everythign gets created      
Base.metadata.create_all(engine)