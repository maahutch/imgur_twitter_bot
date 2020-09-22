# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:30:58 2020

@author: maahutch
"""


import tweepy
import json
from random import shuffle

with open('C:\\Users\\maahutch\\imgur_twitter_bot\\twitter_keys.txt') as json_file:
    keys = json.load(json_file)
    
#Twitter
auth = tweepy.OAuthHandler(
            keys['twitter'][0]['api_key'],
            keys['twitter'][0]['api_secret']
            )
auth.set_access_token(
             keys['twitter'][0]['access_token'],
             keys['twitter'][0]['access_token_secret']
            )
api = tweepy.API(auth, timeout=1000, wait_on_rate_limit=True)



followers_list=[]

for id in  tweepy.Cursor(api.followers_ids, screen_name="RepTrey").pages(-1):
    followers_list.append(id)
    
    
flatten = lambda followers_list: [item for sublist in followers_list for item in sublist]

fl_flat = flatten(followers_list)

shuffle(fl_flat)

to_dm = fl_flat[:5]

for account in to_dm:
    
    target = api.get_user(id=account)       
    fc = target._json['followers_count']

    if  fc < 1000:
        subject = '@'+target._json['screen_name']
        
        api.update_status(status='Hey ' + subject + ' Did you know Congressmen Trey Hollingsworth said more elderly Americans should die from Covid19 to save the economy? https://rb.gy/3xo9xf')