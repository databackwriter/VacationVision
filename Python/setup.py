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




sqldsn, sqlalchemydsn, sqldsn, sqluser, sqlpassword, _ = getDSNfromYAML(PATH_CONNYAML, 0)
_, _, _, mongouser, mongopassword, mongoport = getDSNfromYAML(PATH_CONNYAML, 1)

