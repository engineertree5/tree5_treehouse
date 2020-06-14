#!/usr/local/bin/python3

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Checkin app

# main program will be taking in questions and 

# 2. is there anything you would like to make note of [ yes | no ]
# 3. ?

# constructing API instance
api = tweepy.API(auth)
user = api.get_user('lordfili')

def update_status():
    
    feels = input("TYPE YOUR TWEET BELOW:\n")
    # using tweepy API to update status
    try:
        media = api.media_upload("/Users/MisterFili/Documents/GitHub/tree5_treehouse/tree_types/bot_branch/CHEWY111.png")
        mediaa = api.media_upload("/Users/MisterFili/Documents/GitHub/tree5_treehouse/tree_types/bot_branch/NOK.png")
        api.update_status(status=feels, media_ids=[media.media_id,mediaa.media_id])
        # api.update_status(status=feels)
        print('tweet sent!\n', feels)
    
    except tweepy.TweepError as e:
        print(e.reason)
        print(e.api_code)
        print(e.response.text)

def main():
    update_status()

if __name__ == "__main__":
    main()