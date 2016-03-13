#!/usr/bin/env python2.7
# by Alex Eames http://raspi.tv/?p=5918
# twitterwin.py for twitter access - modified by SJW for testing
import tweepy
import random

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

follow2 = api.followers_ids()  # gives a list of followers ids
print "you have %d followers" % len(follow2)

show_list = raw_input("Do you want to list the followers array?")
if show_list in('y', 'yes', 'Y', 'Yes', 'YES'):
    print follow2

def pick_winner():
    random_number = random.randint(0, len(follow2)-1)
    winner = api.get_user(follow2[random_number])
    print winner.screen_name, random_number

while True:
    pick = raw_input("Press Enter to pick a winner, Q to quit.")
    if pick in ('q', 'Q', 'quit', 'QUIT', 'Quit'):
        break
    pick_winner()
