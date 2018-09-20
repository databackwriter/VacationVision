#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:20:55 2018
A collection of functions for querying Twitter
@author: petermoore
"""

import tweepy
from tweepy import OAuthHandler
consumer_key = "iQkbcIUGmkhLqLBQb5tonpXjd"
consumer_secret = "ozbVURIAUTqRkeVE31gzw8vhf3Od3oY2oM45L5aL5EiNqXE3TI"
access_token = "54530145-LUHaQY9lWRNJicKg16bOaeQKL51ohNTgXBlHzrAjO"
access_secret = "yql7bFUheCIoxXn4OaJmtwQcbIrzSukT4KImlEfjfLVGI"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# following three functions inspired by https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
def gettimeline(username,
                include_rts=False,
                exclude_replies=True):
    tweets = api.user_timeline(screen_name=username,
                               count=200, include_rts=include_rts,
                               exclude_replies=exclude_replies)

    last_id = tweets[-1].id
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

def getimagepath(status):
    media_file = ""
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_file = (media[0]['media_url'])

    return media_file

def downloadfromurl(media_file, filename):
    import wget
    wget.download(url=media_file, out = filename)
    
username = "thedatabloke"
tweets = gettimeline(username)


#for status in tweets:
#    print(status)



hashtag = "#dailyperson"
holdingdir="/Users/petermoore/Documents/GitHub/DailyFrenzy/images/{}.{}"
xlfile = holdingdir.format("ListOfImages", "xlsx")

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

print(i)

#xldf.head()

import pandas as pd

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(xlfile)

# Convert the dataframe to an XlsxWriter Excel object.
xldf.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
