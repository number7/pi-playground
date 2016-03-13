#!/usr/bin/env python2.7
# tweet.py by Alex Eames http://raspi.tv/?p=5908
# modified by SJW for testing
import tweepy
import sys

# consumer keys and access tokens, used for OAuth
consumer_key = 'place consumer key here'
consumer_secret = 'place consumer secret here'
access_token = 'place access token here'
access_token_secret = 'place access token secret here'

# OAuth process, using key and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

if len(sys.argv) >= 2:
    tweet_text = sys.argv[1]

else:
    tweet_text = "This is a test message for posting to Twitter."

if len(tweet_text) <= 140:
    api.update_status(status=tweet_text)
else:
    print "tweet not sent. too long. 140 chars max."
