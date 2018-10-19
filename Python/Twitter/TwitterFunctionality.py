#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:11:12 2018
A collection of functions for interacting with Twitter
Depends on MongoFunctionality
@author: petermoore
"""

from MongoFunctionality import mongoAppend

# get a user's timeline from https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/


def twitterGetTimeline(api,
                       username,
                       include_rts=False,
                       exclude_replies=True
                       ):
    # example usage
    # from setup import twitterapi
    # tweets = twitterGetTimeline(twitterapi, "thedatabloke")
    # for tweet in tweets:
    #    twitterPrintTweetJSON(tweet._json)
    tweets = api.user_timeline(screen_name=username,
                               count=200, include_rts=include_rts,
                               exclude_replies=exclude_replies)

    last_id = tweets[-1].id  # PM: usage is limited to 200 tweets per time
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


def twitterPrintTweetJSON(tweet):
    import json
    print(json.dumps(tweet._json))


def twitterAddTweetJSONtoMongo(tweet):
    return mongoAppend(tweet._json)


username = "kate_is_busy"
tweets = gettimeline(username)






hashtag = "#dailyperson"
holdingdir="/Users/petermoore/Documents/GitHub/DailyFrenzy/images/{}.{}"
xlfile = holdingdir.format("ListOfImages2", "xlsx")

import pandas as pd
xldf = pd.DataFrame()

i = 1
for status in tweets:
    if hashtag in status.text:
        createdstr = str(status.created_at)[:10]
        picturefile = getimagepath(status)
        if len(picturefile) > 0: # build our model
#            df2 = pd.DataFrame([[createdstr, picturefile, status.text]], columns=collist)
            picturefileout = holdingdir.format(createdstr, "jpg")
            rowdict={}
            rowdict["Created"] = createdstr
            rowdict["PictureFileTwitter"] = picturefile
            rowdict["PictureFileLocal"] = createdstr + ".jpg"
            rowdict["Tweet"] = status.text
            xldf = xldf.append(rowdict, ignore_index=True)
            downloadfromurl(picturefile,picturefileout)

    i += 1



xldf.head()


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(xlfile)

# Convert the dataframe to an XlsxWriter Excel object.
xldf.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
