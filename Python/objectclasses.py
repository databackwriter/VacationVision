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

from SQLFunctionality import sqlAppendIfNotExists

# sample class called Version
class Version(Base):
    __tablename__='Version'
    Versionid= Column( Integer, primary_key=True, nullable=False )
    Version= Column( String(50), nullable=False )
    def addappend(self, session):
        return sqlAppendIfNotExists(session, Version,
                                       Version=self.Version)
        
  # where the engine runs and everythign gets created      
Base.metadata.create_all(engine)