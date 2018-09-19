#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:28:58 2018

@author: petermoore
"""
PATH_CONNYAML = "connections.yaml" #NB this file ignored from GitHub
def getDSNfromYAML(yamlfile):
    import yaml
    with open(yamlfile, 'r') as f:
        doc = yaml.load(f)
        pdsn = doc["sqlconn"]["DSN"]
        puser = doc["sqlconn"]["user"]
        ppassword = doc["sqlconn"]["password"]
    dsn="DSN="+pdsn+";UID="+puser+";PWD="+ppassword
    alchemydsn = "mssql+pyodbc://"+puser+":"+ppassword+"@"+pdsn
    return dsn, alchemydsn, pdsn, puser, ppassword



import os
print(os.getpwd())