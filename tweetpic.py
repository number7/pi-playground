#!/usr/bin/env python2.7
# tweetpic.py - modified by SJW to post an image file
# by Alex Eames http://raspi.tv/?p=5918
import tweepy
from subprocess import call
from datetime import datetime
 
i = datetime.now()               #take time and date for filename
# now = i.strftime('%Y%m%d-%H%M%S')
photo_name = 'penguin-test.jpg'

# Consumer keys and access tokens, used for OAuth
consumer_key = 'place consumer key here'
consumer_secret = 'place consumer secret here'
access_token = 'place access token here'
access_token_secret = 'place access token secret here'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Send the tweet with photo
photo_path = '/home/pi/code/python/' + photo_name
status = 'Photo tweet from the PI: ' + i.strftime('%Y/%m/%d %H:%M:%S') 
api.update_with_media(photo_path, status=status)
