#!/usr/local/bin/python3

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Checkin app

# main program will be taking in questions and 

# 1. would you like to send a tweet as a bot [yes | no ]
# 2. is there anything you would like to make note of [ yes | no ]
# 3. ?

# constructing API instance
api = tweepy.API(auth)
user = api.get_user('lordfili')


def user_feels():
    feels = input("what would you like to twwet?")
    return feels
def update_status(n):
    # using tweepy API to update status

    print(n)
    # try:
    #     api.update_status(status=statement)
    
    # except tweepy.TweepError as e:
    #     print(e.reason)
    #     print(e.api_code)
    #     print(e.response.text)


update_status(user_feels())