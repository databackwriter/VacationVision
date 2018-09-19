#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:06:20 2018

@author: petermoore
"""

from setup import sqlAppendIfNotExists, Base

from sqlalchemy import Column, Integer, String
class Section(Base):
    __tablename__='Section'
    sectionid= Column( Integer, primary_key=True, nullable=False )
    section= Column( String(50), nullable=False )
    def addappend(self, session):
        return sqlAppendIfNotExists(session, Section,
                                       section=self.section)