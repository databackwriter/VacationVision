#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:51:20 2018

@author: petermoore
"""

import tensorflow as tf
hello=tf.constant("yo")
sess=tf.Session()
print(sess.run(hello))


pwd="/Users/petermoore/Documents/GitHub/VacationVision/GCP/cloudml-samples-master/census/estimator/data/"


TRAIN_DATA=pwd+"adult.data.csv"
TEST_DATA=pwd+"adult.test.csv"

MODEL_DIR = pwd+"output"


from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

ml = discovery.build('ml','v1')
projectIDshort = 'vacationvision-216515'
projectID = 'projects/{}'.format(projectIDshort)
modelname = "model" + projectIDshort.replace("-","")
uri = "https://ml.googleapis.com/v1/" + projectID + "/models"



requestDict = {'name': modelname,
               'description': 'This is a machine learning model entry.'}


request = ml.projects().models().create(parent=projectID,
                     body=requestDict)
from googleapiclient import errors

try:
    response = request.execute()
    print(response)

except errors.HttpError as err:
    # Something went wrong, print out some information.
    print('There was an error creating the model. Check the details:')
    print(err._get_reason())


#gcloud ml-engine local train \
#    --module-name trainer.task \
#    --package-path trainer/ \
#    --job-dir $MODEL_DIR \
#    -- \
#    --train-files $TRAIN_DATA \
#    --eval-files $EVAL_DATA \
#    --train-steps 1000 \
#    --eval-steps 100