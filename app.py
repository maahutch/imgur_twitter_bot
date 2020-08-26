# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:25:34 2020

@author: maahutch
"""


from imgurpython import ImgurClient
from PIL import Image
from urllib.request import urlopen
import tweepy
import json
import os
from random import shuffle

with open('twitter_keys.txt') as json_file:
    keys = json.load(json_file)


#Imgur
client_id     = keys['imgur'][0]['client_id']
client_secret = keys['imgur'][0]['client_secret']

client = ImgurClient(client_id, client_secret)

items=client.gallery(window='hour')

shuffle(items)

tags_list = []

keyWords=['politics', 'vote', 'capitalism','trump', 'current events']

keyWords2 = ['funny']

index = 0

size = len(items)


while index < size:
    one_item = items[index].tags
    try:
        tags_list.append(one_item[0]['name'])
        for i in tags_list:
            i.lower
            if i in keyWords:
                current_image = items[index].images[0]['link']
                break
            else:
                pass
    except:
        pass
    index += 1
    
index = 0

try:
    current_image
except NameError:
    one_item = items[index].tags
    try:
        tags_list.append(one_item[0]['name'])
        for i in tags_list:
            i.lower
            if i in keyWords2:
                current_image = items[index].images[0]['link']
                break
            else:
                pass
    except:
        pass
    index += 1
    


img_raw = Image.open(urlopen(current_image))
img = img_raw.convert('RGB')
img.save("current_image.jpg")


#Twitter

auth = tweepy.OAuthHandler(
            keys['twitter'][0]['api_key'],
            keys['twitter'][0]['api_secret']
            )
auth.set_access_token(
             keys['twitter'][0]['access_token'],
             keys['twitter'][0]['access_token_secret']
            )
api = tweepy.API(auth)

#Get Trending Hashtags

USA=23424977
usa_trends = api.trends_place(USA)
trends = json.loads(json.dumps(usa_trends, indent = 1))


trend_tags = []
for i in trends[0]["trends"]:
    trend_tags.append(i['name'])

#hashtags = ["#"+tag for tag in tags_list]

#tweet1 = ' '.join(hashtags)
tweet2 = ' '.join(trend_tags)
#tweet = str(tweet1 + ' ' + tweet2)
tweet = tweet2[0:279]

media = api.media_upload("current_image.jpg")

post_result = api.update_status(status=tweet, media_ids=[media.media_id])

os.remove("current_image.jpg")

